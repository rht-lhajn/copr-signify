Name:           signify
Version:        31
Release:        1%{?dist}
Summary:        Cryptographically sign and verify files

License:        ISC
URL:            https://github.com/aperezdc/%{name}
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.xz.asc
Source2:        gpgkey-5AA3BC334FD7E3369E7C77B291C559DBE4C9123B.gpg

Patch0:         signify-freezero.patch

BuildRequires: make
BuildRequires: gcc
BuildRequires: libbsd-devel >= 0.8.0
BuildRequires: gnupg2
Requires: libbsd >= 0.8.0

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

%global _hardened_build 1

%description
OpenBSD tool which enables user to sign and verify signatures on files.
A signature verifies the integrity of a message.

The signify utility exits 0 on success, and >0 if an error occurs.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q

# Strip bundled libraries
rm -rf libwaive

%patch0

%build
%set_build_flags
%make_build GIT_TAG=''


%install
%make_install DESTDIR=%{buildroot}%{_prefix} \
  docdir=%{_pkgdocdir} \
  GIT_TAG=''

# Docs
mkdir -p %{buildroot}%{_pkgdocdir}
install -m644 -p README.md CHANGELOG.md \
  %{buildroot}%{_pkgdocdir}


%check
%{__make} check GIT_TAG=''


%files
%license COPYING
%{_pkgdocdir}
%{_bindir}/signify
%{_mandir}/man?/*


%changelog
* Wed May 4 2022 Lukas Hajn <lhajn@redhat.com> - 31-1
- updated to v31

* Thu Sep 24 2020 Lukas Hajn <lhajn@redhat.com> - 30-1
- updated to v30

* Mon Feb 24 2020 Lukas Hajn <lhajn@redhat.com> - 29-1
- updated to v29
- removed external license

* Mon Feb 24 2020 Lukas Hajn <lhajn@redhat.com> - 28-2
- added check

* Fri Feb 21 2020 Lukas Hajn <lhajn@redhat.com> - 28-1
- initial release

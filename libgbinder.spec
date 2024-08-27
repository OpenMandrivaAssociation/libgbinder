%define _empty_manifest_terminate_build 0

%define libname %mklibname gbinder
%define devname %mklibname -d gbinder

Name:           libgbinder
Version:        1.1.40
Release:        1
Summary:        GLib-style interface to binder
License:        BSD-3-Clause
URL:            https://github.com/mer-hybris/libgbinder
Source0:        https://github.com/mer-hybris/libgbinder/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz
Source1:        gbinder.conf
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libglibutil)

%description
GLib-style interface to binder (Android IPC mechanism)

%package -n %{libname}
Summary:        Library for %{name}

%description -n %{libname}
Library for %{name}.

%package -n %{devname}
Summary:        Development library for %{name}
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
This package contains the development library for %{name}.

%prep
%autosetup

%build
%make_build \
 LIBDIR=%{_libdir} \
 KEEP_SYMBOLS=1 \
 release \
 pkgconfig

%install
%make_install \
 LIBDIR=%{_libdir} \
 DESTDIR=%{buildroot} \
 install-dev
 
install -Dm 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/gbinder.conf
mkdir %{buildroot}%{_sysconfdir}/gbinder.d

%files -n %{libname}
%doc AUTHORS README
%license LICENSE
%{_libdir}/%{name}.so.*
%dir %{_sysconfdir}/gbinder.d
%config(noreplace) %{_sysconfdir}/gbinder.conf

%files -n %{devname}
%{_libdir}/pkgconfig/*.pc
%{_libdir}/%{name}.so
%dir %{_includedir}/gbinder
%{_includedir}/gbinder/*.h

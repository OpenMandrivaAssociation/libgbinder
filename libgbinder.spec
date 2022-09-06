%global libname libgbinder1
Name:           libgbinder
Version:        master
Release:        0
Summary:        GLib-style interface to binder
License:        BSD-3-Clause
URL:            https://github.com/mer-hybris/libgbinder
Source0:        _service
Source1:        gbinder.conf
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  libglibutil-devel
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
GLib-style interface to binder (Android IPC mechanism)

%package -n %{libname}
Summary:        Library for %{name}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description -n %{libname}
Library for %{name}.

%package devel
Summary:        Development library for %{name}
Requires: %{libname} = %{version}

%description devel
This package contains the development library for %{name}.

%prep
%autosetup -n %{_sourcedir}/%{name}-%{version} -T -D

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

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%doc AUTHORS README
%license LICENSE
%{_libdir}/%{name}.so.*
%dir %{_sysconfdir}/gbinder.d
%config(noreplace) %{_sysconfdir}/gbinder.conf

%files devel
%{_libdir}/pkgconfig/*.pc
%{_libdir}/%{name}.so
%dir %{_includedir}/gbinder
%{_includedir}/gbinder/*.h

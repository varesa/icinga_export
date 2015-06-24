Name:		icinga_export
Version:	1.0.0	
Release:	1%{?dist}
BuildArch:	noarch
Summary:	A read only interface for data from Icinga2
Group: 		System Environment/Base
License:	GPLv2+
URL:		https://github.com/varesa/icinga_export
Source0: 	%{name}-%{version}.tar.gz

Requires: httpd mod_wsgi

%description

%prep
%autosetup

%build

%install
install -m 644 -D config/httpd.confd %{buildroot}/etc/httpd/conf.d/icinga_export.conf

install -m 755 -d %{buildroot}/var/www/icinga_export
find ./ -name "*.py" -exec install -m 644 {} %{buildroot}/var/www/icinga_export/{} \;

%files
/etc/*
/var/*

%changelog

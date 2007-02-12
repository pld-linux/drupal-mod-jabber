%define		modname jabber
Summary:	Drupal Jabber Authentication Module
Summary(pl.UTF-8):	Moduł uwierzytelnienia Jabbera dla Drupala
Name:		drupal-mod-%{modname}
Version:	4.6.0
Release:	0.1
License:	GPL / GPL v2
Group:		Applications/WWW
Source0:	http://ejabberd.jabber.ru/files/site/jabber.module.txt
# Source0-md5:	6e61b4734e521cbeb203825cf54fc5f2
URL:		http://drupal.org/node/5076
Requires:	drupal >= 4.6.0
Requires:	php(xml)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_drupaldir	%{_datadir}/drupal
%define		_moddir		%{_drupaldir}/modules

%description
Drupal Jabber Authentication Module.

%description -l pl.UTF-8
Moduł uwierzytelnienia Jabbera dla Drupala.

%prep
%setup -qcT
cp -a %{SOURCE0} jabber.module

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_moddir}
install *.module $RPM_BUILD_ROOT%{_moddir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_moddir}/*.module

# TODO
# - localize files
# - system ckeditor
%define		status		stable
%define		pearname	Horde_Editor
Summary:	%{pearname} - Horde Editor API
Name:		php-horde-Horde_Editor
Version:	1.0.0
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.horde.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	abbd163109e96827b9466fcc5aaf4800
URL:		https://github.com/horde/horde/tree/master/framework/Editor/
BuildRequires:	php-channel(pear.horde.org)
BuildRequires:	php-horde-Horde_Role
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.7.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php-channel(pear.horde.org)
Requires:	php-horde-Horde_Browser < 2.0.0
Requires:	php-horde-Horde_Core < 2.0.0
Requires:	php-horde-Horde_Exception < 2.0.0
Requires:	php-horde-Horde_Serialize < 2.0.0
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		hordedir	/usr/share/horde

%description
The Horde_Editor package provides an API to generate the code
necessary for embedding javascript RTE editors in a web page.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

mv ./%{php_pear_dir}/www/horde .

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{hordedir}}
%pear_package_install

cp -a horde/* $RPM_BUILD_ROOT%{hordedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%{php_pear_dir}/.registry/.channel.*/*.reg
%{php_pear_dir}/Horde/Editor
%{php_pear_dir}/Horde/Editor.php

%{hordedir}/js/LICENSE.html
%{hordedir}/js/ckeditor.js
%{hordedir}/js/ckeditor_basic.js
%{hordedir}/js/config.js
%{hordedir}/js/contents.css
%{hordedir}/js/images/spacer.gif

%dir %{hordedir}/js/lang
%{hordedir}/js/lang/*.js

%{hordedir}/js/plugins/a11yhelp
%{hordedir}/js/plugins/about
%{hordedir}/js/plugins/autogrow
%{hordedir}/js/plugins/clipboard
%{hordedir}/js/plugins/colordialog
%{hordedir}/js/plugins/dialog
%{hordedir}/js/plugins/div
%{hordedir}/js/plugins/find
%{hordedir}/js/plugins/flash
%{hordedir}/js/plugins/forms
%{hordedir}/js/plugins/iframedialog
%{hordedir}/js/plugins/image
%{hordedir}/js/plugins/link
%{hordedir}/js/plugins/liststyle
%{hordedir}/js/plugins/pagebreak
%{hordedir}/js/plugins/pastefromword
%{hordedir}/js/plugins/pastetext
%{hordedir}/js/plugins/scayt
%{hordedir}/js/plugins/showblocks
%{hordedir}/js/plugins/smiley
%{hordedir}/js/plugins/specialchar
%{hordedir}/js/plugins/styles
%{hordedir}/js/plugins/syntaxhighlight
%{hordedir}/js/plugins/table
%{hordedir}/js/plugins/tableresize
%{hordedir}/js/plugins/tabletools
%{hordedir}/js/plugins/templates
%{hordedir}/js/plugins/uicolor
%{hordedir}/js/plugins/wsc

%dir %{hordedir}/js/skins
%{hordedir}/js/skins/kama
%{hordedir}/js/skins/office2003
%{hordedir}/js/skins/v2
%{hordedir}/js/themes/default/theme.js

%define rname rmail
%define oname rubymail
%define name  ruby-%{rname}

%define version 0.17
%define release %mkrel 2

Summary: An Email/MIME library for Ruby
Name: %name
Version: %version
Release: %release
License: BSD-like
Group: Development/Ruby
URL: http://www.lickey.com/rubymail/
Source0: http://www.lickey.com/rubymail/download/%{oname}-%{version}.tar.bz2
BuildArch: noarch
BuildRequires: ruby 
Requires: ruby
Provides: %{oname}

%description
This is RubyMail, a lightweight mail library containing various mail utility
classes and modules.

Very high attention is paid to quality and robustness. This package has a
complete unit test suite (requires RubyUnit to run).

%prep
%setup -q -n %{oname}-%{version}

%build
ruby install.rb config
ruby install.rb setup
ruby tests/runtests.rb

%clean
rm -rf %buildroot

%install
rm -rf %buildroot
ruby install.rb install --prefix=%buildroot

%files
%defattr(-,root,root)
%{ruby_sitelibdir}/%{rname}*
%doc NEWS NOTES README THANKS TODO doc/ guide/


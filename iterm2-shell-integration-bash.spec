%global commit 67e9313f992f824f5102491fcb587611ba948035
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global upstream_github gnachman
%global upstream_name iterm2-website


Summary: iTerm2 Shell Integration
Name: iterm2-shell-integration-bash
Version: 0
Release: 0.1.20220717git%{shortcommit}%{?dist}
License: GPLv2
URL: https://iterm2.com/documentation-shell-integration.html

Source0: https://github.com/%{upstream_github}/%{upstream_name}/archive/%{commit}/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch: noarch


%description
iTerm2 may be integrated with the unix shell so that it can keep track
of your command history, current working directory, host name, and
more—even over ssh. This enables several useful features.


%prep
%autosetup -n %{upstream_name}-%{commit}
# remove first line (shebang)
sed -i 1d source/shell_integration/bash

%build
# Nothing to do

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__install} -Dp -m0644 source/shell_integration/bash \
  $RPM_BUILD_ROOT%{_sysconfdir}/profile.d/iterm2.sh

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%{_sysconfdir}/profile.d/iterm2.sh

%changelog
* Fri May 28 2021 Danila Vershinin <info@getpagespeed.com> 0-0.1.20210528gitbe9d982
- Initial packaging

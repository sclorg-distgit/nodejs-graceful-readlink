%{?scl:%scl_package nodejs-graceful-readlink}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

%global packagename graceful-readlink
%global enable_tests 0
# there is no test suite on this package, but we can still do some self-tests

Name:		%{?scl_prefix}nodejs-graceful-readlink
Version:	1.0.1
Release:	3%{?dist}
Summary:	The graceful fs.readlink functionality

License:	MIT
URL:		https://github.com/zhiyelee/graceful-readlink.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz

ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch

BuildRequires:	%{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
%endif

%description
The graceful fs.readlink functionality

%prep
%setup -q -n package

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

#%if 0%{?enable_tests}
#%check
#%nodejs_symlink_deps --check
# do a quick self-test on the module
#%{__nodejs} -e 'require("./")'
#%endif

%files
%{!?_licensedir:%global license %doc}
%doc *.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}

%changelog
* Wed Sep 21 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.1-3
- Built for RHSCL

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 21 2015 Jared Smith <jsmith@fedoraproject.org> - 1.0.1-1
- Initial packaging

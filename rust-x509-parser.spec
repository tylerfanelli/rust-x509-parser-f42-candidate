# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate x509-parser

Name:           rust-x509-parser
Version:        0.16.0
Release:        %autorelease
Summary:        X.509 v3 parser library

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/x509-parser
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Parser for the X.509 v3 format (RFC 5280 certificates).}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
%doc %{crate_instdir}/CHANGELOG.md
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+ring-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+ring-devel %{_description}

This package contains library source intended for building other packages which
use the "ring" feature of the "%{crate}" crate.

%files       -n %{name}+ring-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+validate-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+validate-devel %{_description}

This package contains library source intended for building other packages which
use the "validate" feature of the "%{crate}" crate.

%files       -n %{name}+validate-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+verify-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+verify-devel %{_description}

This package contains library source intended for building other packages which
use the "verify" feature of the "%{crate}" crate.

%files       -n %{name}+verify-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
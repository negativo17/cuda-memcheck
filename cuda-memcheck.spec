%global real_name cuda_memcheck

%global debug_package %{nil}
%global __strip /bin/true
%global _missing_build_ids_terminate_build 0
%global _build_id_links none
%global major_package_version 11-6

Name:           %(echo %real_name | tr '_' '-')
Epoch:          1
Version:        11.6.55
Release:        1%{?dist}
Summary:        CUDA run time error detection tool for CUDA applications
License:        CUDA Toolkit
URL:            https://developer.nvidia.com/cuda-toolkit
ExclusiveArch:  x86_64 ppc64le

Source0:        https://developer.download.nvidia.com/compute/cuda/redist/%{real_name}/linux-x86_64/%{real_name}-linux-x86_64-%{version}-archive.tar.xz
Source1:        https://developer.download.nvidia.com/compute/cuda/redist/%{real_name}/linux-ppc64le/%{real_name}-linux-ppc64le-%{version}-archive.tar.xz

Conflicts:      %{name}-%{major_package_version} < %{?epoch:%{epoch}:}%{version}-%{release}
 
%description
CUDA-MEMCHECK is a functional correctness checking suite included in the CUDA
toolkit. This suite contains multiple tools that can perform different types of
checks.

CUDA-MEMCHECK can be run in standalone mode where the user's application is
started under CUDA-MEMCHECK. The memcheck tool can also be enabled in integrated
mode inside CUDA-GDB.

CUDA-MEMCHECK is deprecated and will be removed in a future release of the CUDA
toolkit. Please use the compute-sanitizer as a drop-in replacement.

%prep
%ifarch x86_64
%setup -q -n %{real_name}-linux-x86_64-%{version}-archive
%endif

%ifarch ppc64le
%setup -q -T -b 1 -n %{real_name}-linux-ppc64le-%{version}-archive
%endif

%install
install -m 0755 -p -D bin/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%{_bindir}/%{name}

%changelog
* Tue Jan 25 2022 Simone Caronni <negativo17@gmail.com> - 1:11.6.55-1
- First build with the new tarball components.


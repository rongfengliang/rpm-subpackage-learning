# rpm subpackage learning

## build

```code
rpmbuild -ba foo-2.7.spec 
```

## view content info

```code
rpm -qip ~/rpmbuild/RPMS/x86_64/foo-client-2.7-1.x86_64.rpm
```
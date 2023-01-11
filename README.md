# Retrieve Windows OEM Product Key!
PC producers like HP, Dell and many more give an inbuilt os with an activated os with a key, that key is known as OEM key.

You can retrieve this key even after you have booted Linux on the system. This repository tries to fetch the same on Linux as well as on Windows, because some of us forget to note that stuff down before jumping in to install Arch.


# Running

On Linux, you can retrieve the Windows OEM Product Key by reading the `MSDM` table. You can fetch the key by running:

```python
$ sudo ./fetcher.py
```

On Windows, you can still fetch the key by running the following from an elevated prompt:

```powershell
> python3 fetcher.py
```

# Tested On:
- Lenovo Legion (Arch)
- HP Pavilion (Dell)
- DELL (Fedora)

Help to expand this list?
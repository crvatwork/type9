[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/timway/type9)

# Type9

A tool that is meant to easily generate password hashes in the format used by Cisco networking devices for validating passwords of users local to the device. A common use for this tool is to generate hashes for a known password when creating device templates.

## Run in a container

A container is an ideal way to execute this tool because not all Linux distributions make the scrypt python module easily available. Running in a container abstracts the dependencies away and enables the user of the tool to quickly and reliably generate the hash value they need to perform their task.

It can simply be run at the CLI with a given plain-text password to generate a pseudo random salt and use that to build the has with this simple command:

```bash
docker run --rm -it timway/type9 PlainTextPassword
```

It can be passed a specific salt value like so:

```bash
docker run --rm -it timway/type9 eM53DRPA3ClnY2 PlainTextPassword
```

If you'd like to store the hash value of a password in an environment variable, possibly for usage in a template use this command:

```bash
HASH=`docker run --rm -it timway/type9 eM53DRPA3ClnY2 PlainTextPassword`
```

You can consume for example like this:

```bash
echo "username type9 privilege 15 ${HASH}"
```

## Install into the local Python environment
The tool can be installed via setuptools into the user, global or virtual environment using the following command:

```bash
python setup.py install
```

The parameters are the same as the example in a container above.

```bash
type9 PlainTextPassword
type9 eM53DRPA3ClnY2 PlainTextPassword
```

## Binaries
Currently binaries are not available. This may change in the future.

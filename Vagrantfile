# -*- mode: ruby -*-
# vi: set ft=ruby :

#
# REQUIREMENTS:
#   see install.md
#

# Minimum required Vagrant version
Vagrant.require_version ">= 1.6.5"

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # Every Vagrant virtual environment requires a box to build off.
  # INFO: https://vagrantcloud.com/hansode/boxes/centos-6.6-x86_64
  config.vm.box = "hansode/centos-6.6-x86_64"

  # Install renter on the box
  config.vm.provision :shell, path: "./bin/vagrant-provision"

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  config.vm.network "forwarded_port", guest: 5001, host: 5001

  config.vm.post_up_message = "pylibukin sandbox installed"
end


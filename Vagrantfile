# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.
  
  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  config.vm.box = "generic/debian10"
  config.vm.box_version = "3.4.2"

  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # NOTE: This will enable public access to the opened port
  
  # config.vm.network "public_network"
  
  config.vm.network "forwarded_port", guest: 8123, host: 8123
  config.vm.network "forwarded_port", guest: 3000, host: 3000
  config.vm.network "forwarded_port", guest:  137, host:  137
  config.vm.network "forwarded_port", guest:  138, host:  138
  config.vm.network "forwarded_port", guest:  139, host:  139
  config.vm.network "forwarded_port", guest:  445, host:  445
  config.vm.network "forwarded_port", guest: 8086, host: 8086

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine and only allow access
  # via 127.0.0.1 to disable public access
  # config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network "private_network", ip: "192.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  config.vm.synced_folder ".", "/vagrant", mount_options: ["rw"], automount: true

  config.vm.provider "virtualbox" do |v|
    v.memory = 1024
    v.cpus = 2
    v.customize ["modifyvm", :id, "--vram", "16"]
    #v.customize ["modifyvm", :id, "--paravirtprovider", "kvm"]
    #v.customize ["modifyvm", :id, "--longmode", "off"]
    #v.customize ["modifyvm", :id, "--vtxvpid", "off"]
    #v.customize ["modifyvm", :id, "--vtxux", "off"]
    #v.customize ["modifyvm", :id, "--hwvirtex", "on"]
    v.customize ["modifyvm", :id,"--nested-hw-virt", "on"]
  end
  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  # config.vm.provider "virtualbox" do |vb|
  #   # Display the VirtualBox GUI when booting the machine
  #   vb.gui = true
  #
  #   # Customize the amount of memory on the VM:
  #   vb.memory = "1024"
  # end
  #
  # View the documentation for the provider you are using for more
  # information on available options.

  config.vm.provision "shell", path: 'vagrant-provision.sh'
  config.vm.provision "ansible_local" do |ansible|
    ansible.playbook = "playbook.yml" 
    ansible.galaxy_role_file = "requirements.yaml"
    ansible.galaxy_command = "ansible-galaxy install --force -r %{role_file} "
  end
  # Enable provisioning with a shell script. Additional provisioners such as
  # Ansible, Chef, Docker, Puppet and Salt are also available. Please see the
  # documentation for more information about their specific syntax and use.
  # config.vm.provision "shell", inline: <<-SHELL
  #   apt-get update
  #   apt-get install -y apache2
  # SHELL
end

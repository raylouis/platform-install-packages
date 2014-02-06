#
# Cookbook Name:: kaltura
# Recipe:: default
#
# Copyright 2014, Kaltura, Ltd.
#
log "Installing Kaltura all in 1"
package "kaltura-server" do
  action :install
 end
#%w{ apr apr-util lynx }.each do |pkg|
#  package pkg do
#    action :install
#  end
#end
template "/root/kaltura.ans" do
    source "kaltura.ans.erb"
    mode 0600
    owner "root"
    group "root"
end

bash "setup DWH " do
     user "root"
     code <<-EOH
	"#{node[:kaltura][:install_root]}"/bin/kaltura-config-all.sh /root/kaltura.ans
     EOH
end

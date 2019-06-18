
官网下载 https://www.vagrantup.com 

下载镜像的方式
https://app.vagrantup.com/centos/boxes/7/versions/1804.02/providers/virtualbox.box
下载链接 = 产品版本链接 + 供应商英文意思 + 要下载的供应商名称（如virtualbox）+'.box'
由于国内没有快的镜像源，可以通过迅雷 先下载到本地 

1.init  
`vagrant init hashicorp/precise64`  

2.add  
`vagrant box  add ashicorp/precise64 /localaddr`

3.start  
`vagrant up`

4.connect  
`vagrant ssh`


创建HelloWorld项目
    django-admin startproject HelloWorld   
    其中目录下的HelloWorld目录为项目的容器：
    settings.py ： 包含了项目的默认设置，包括数据库信息，调试标志以及其他一些工作的变量。
    urls.py ： 负责把URL模式映射到应用程序。
    wsgi.py :  用于项目部署。
    manage.py: 一个实用的命令行工具，可让你以各种方式与该 Django 项目进行交互。
    templates目录存放html网页，修改 TEMPLATES 中的 DIRS 为 [BASE_DIR+"/templates",]，寻找网页的路径
    static目录中存放js以及css文件    
启动服务器：
    python manage.py runserver 0.0.0.0:8000

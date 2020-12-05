from flask import Flask, jsonify, request, render_template
from config import SQLALCHEMY_DATABASE_URI
from flask_sqlalchemy import SQLAlchemy
import pymysql
import requests
import json
from datetime import datetime
import re
from random import randint
# from flask_cors import *



app = Flask(__name__)
# CORS(app, supports_credentials=True)  # 设置跨域
app.config['JSON_AS_ASCII'] = False
# app.config.from_object(config)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)
pymysql.install_as_MySQLdb()



class BaseModel(object):
    """模型类的基类，为每个模型补充创建时间和更新时间"""
    # 记录创建的时间
    create_time = db.Column(db.DateTime, default=datetime.now)
    # 记录更新的时间
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

# 网站信息表
class WebsiteInfos(BaseModel, db.Model):
    __tablename__ = 'video_website_infos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ip_id = db.Column(db.Integer, db.ForeignKey('video_server_ips.id'))
    url = db.Column(db.String(128), nullable=False)
    is_activate = db.Column(db.Boolean, default=True, nullable=False)
    title = db.Column(db.String(128))
    keywords = db.Column(db.String(128))
    description = db.Column(db.String(128))
    baidu_code = db.Column(db.String(256))  # 百度统计代码


# 联系方式
class ContactInfos(BaseModel, db.Model):
    __tablename__ = 'video_contact_infos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tool = db.Column(db.String(32), nullable=False)
    info = db.Column(db.String(128), nullable=False)


# 广告信息表： 只需要保存两个信息，target_url和img_url
class AdsInfos(BaseModel, db.Model):
    __tablename__ = 'video_ads_infos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    target_url = db.Column(db.String(256), nullable=False)
    img_url = db.Column(db.String(256), nullable=False)
    ads_kind = db.Column(db.Integer, db.ForeignKey('video_ads_kinds.id'))  # 一类的表明.id

# 首页
@app.route('/',methods=['GET'])
def index():
    print('url_root = ', request.url_root)
    print('url = ', request.url)
    infos = get_infos_from_database_by_url(request.url_root)
    if len(infos['ads_left_right_infos']) > 0:
        left_right = infos['ads_left_right_infos'][randint(0, len(infos['ads_left_right_infos'])-1)]
    else:
        left_right = ''

    if len(infos['ads_top_bottom_infos']) > 0:
        top_bottom = infos['ads_top_bottom_infos'][randint(0, len(infos['ads_top_bottom_infos'])-1)]
    else:
        top_bottom = ''
    context = {
        'url':infos['web_infos'].url,
        'title':infos['web_infos'].title,
        'keywords': infos['web_infos'].keywords,
        'description': infos['web_infos'].description,
        'baidu_code': infos['web_infos'].baidu_code,
        'contact_infos':infos['contact_infos'],
        'ads':{
            'top': infos['ads_top_infos'],
            'bottom': infos['ads_bottom_infos'],
            'left_right': left_right,
            'top_bottom' top_bottom:
        },
        'cates': [],  # 其中元素：{‘id’:***, 'text':***,'class_details_20':[{***},{***}]}
        'videos':[]
    }

    resp_cates = requests.get('http://shayuapi.com/api.php/provide/vod/at/json')
    # print("resp_cates.text = ", json.loads(resp_cates.text, encoding='utf-8'))
    if resp_cates.status_code == 200:
        resp_cates_json = json.loads(resp_cates.text, encoding='utf-8')
        for cate in resp_cates_json.get('class'):
            context['cates'].append(cate)
    resp_latest = requests.get('http://shayuapi.com/api.php/provide/vod/at/json/?ac=detail&h=24')
    if resp_latest.status_code == 200:
        resp_latest_json = json.loads(resp_latest.text, encoding='utf-8')
        # print("resp_latest_json = ", resp_latest_json)
        for temp in resp_latest_json.get('list'):
            video = {
                'type_id': temp.get('type_id'),
                'type_name': temp.get('type_name'),
                'vod_id': temp.get('vod_id'),
                'vod_name': temp.get('vod_name'),
                'vod_tag': temp.get('vod_tag'),
                'vod_pic': temp.get('vod_pic'),
                'vod_time': temp.get('vod_time'),
                'vod_play_url': temp.get('vod_play_url').split('$')[1]
            }
            context['videos'].append(video)
    # return jsonify(context)
    # print("context = ", context)
    return render_template('/index.html', context=context)

def isDigit(x):
    try:
        x=int(x)
        return isinstance(x,int)
    except ValueError:
        return False


# 分类页面, 注意分页 /cate/1?page=2
@app.route('/cate/<int:cate_id>', methods=['GET'])
def cate(cate_id):
    # print('url_root = ', request.url_root)
    # print('url = ', request.url)
    if request.args.get('page') == None:
        page = 1
    elif isDigit(request.args.get('page')) == False:
        return 'page type error'
    else:
        page = int(request.args.get('page'))
    # print("page = ", page)
    infos = get_infos_from_database_by_url(request.url_root)
    if len(infos['ads_left_right_infos']) > 0:
        left_right = infos['ads_left_right_infos'][randint(0, len(infos['ads_left_right_infos'])-1)]
    else:
        left_right = ''

    if len(infos['ads_top_bottom_infos']) > 0:
        top_bottom = infos['ads_top_bottom_infos'][randint(0, len(infos['ads_top_bottom_infos'])-1)]
    else:
        top_bottom = ''
    context = {
        'url':infos['web_infos'].url,
        'title':infos['web_infos'].title,
        'keywords': infos['web_infos'].keywords,
        'description': infos['web_infos'].description,
        'baidu_code': infos['web_infos'].baidu_code,
        'contact_infos':infos['contact_infos'],
        'ads':{
            'top': infos['ads_top_infos'],
            'bottom': infos['ads_bottom_infos'],
            'left_right': left_right,
            'top_bottom': top_bottom
        },
        'cates': [],  # 其中元素：{‘id’:***, 'text':***,'class_details_20':[{***},{***}]}
        'videos':[],
        'pageinfo':{
            'page_activate':page, # 当前页
            'page_total': ''
        }
    }
    cates_ids = []
    pagecount = ''
    resp_cates = requests.get('https://shayuapi.com/api.php/provide/vod/at/json?t='+str(cate_id))
    if resp_cates.status_code == 200:
        resp_cates_json = json.loads(resp_cates.text, encoding='utf-8')
        pagecount = resp_cates_json.get('pagecount')
        for cate in resp_cates_json.get('class'):
            context['cates'].append(cate)
            cates_ids.append(cate.get('type_id'))
    if cate_id not in  cates_ids:
        return 'error id!'
    # print('pagecount= ', pagecount)
    if page > pagecount:
        return 'page is biger than pagecount'
    context['pageinfo']['page_total'] = pagecount
    # print('detail url = ', 'https://shayuapi.com/api.php/provide/vod/at/json/?ac=detail&pg='+str(pagecount-page)+'&t='+str(cate_id)+'')
    resp_latest = requests.get('https://shayuapi.com/api.php/provide/vod/at/json/?ac=detail&pg='+str(pagecount-page)+'&t='+str(cate_id)+'')
    if resp_latest.status_code == 200:
        resp_latest_json = json.loads(resp_latest.text, encoding='utf-8')
        for temp in resp_latest_json.get('list'):
            video = {
                'type_id': temp.get('type_id'),
                'type_name': temp.get('type_name'),
                'vod_id': temp.get('vod_id'),
                'vod_name': temp.get('vod_name'),
                'vod_tag': temp.get('vod_tag'),
                'vod_pic': temp.get('vod_pic'),
                'vod_time': temp.get('vod_time'),
                'vod_play_url': temp.get('vod_play_url').split('$')[1]
            }
            context['videos'].append(video)
    # return jsonify(context)
    # print("context = ", context)
    return render_template('/cate.html', context=context)


# 详情页
@app.route('/detail/<int:detail_id>', methods=['GET'])
def detail(detail_id):
    # print('url_root = ', request.url_root)
    # print('url = ', request.url)
    infos = get_infos_from_database_by_url(request.url_root)
    if len(infos['ads_left_right_infos']) > 0:
        left_right = infos['ads_left_right_infos'][randint(0, len(infos['ads_left_right_infos'])-1)]
    else:
        left_right = ''

    if len(infos['ads_top_bottom_infos']) > 0:
        top_bottom = infos['ads_top_bottom_infos'][randint(0, len(infos['ads_top_bottom_infos'])-1)]
    else:
        top_bottom = ''
    context = {
        'url':infos['web_infos'].url,
        'title':infos['web_infos'].title,
        'keywords': infos['web_infos'].keywords,
        'description': infos['web_infos'].description,
        'baidu_code': infos['web_infos'].baidu_code,
        'contact_infos':infos['contact_infos'],
        'ads':{
            'top': infos['ads_top_infos'],
            'bottom': infos['ads_bottom_infos'],
            'left_right': left_right,
            'top_bottom': top_bottom
        },
        'cates': [],  # 其中元素：{‘id’:***, 'text':***,'class_details_20':[{***},{***}]}
        'video':''
    }
    resp_cates = requests.get('https://shayuapi.com/api.php/provide/vod/at/json/')
    if resp_cates.status_code == 200:
        resp_cates_json = json.loads(resp_cates.text, encoding='utf-8')
        for cate in resp_cates_json.get('class'):
            context['cates'].append(cate)
    resp_latest = requests.get('https://shayuapi.com/api.php/provide/vod/at/json/?ac=detail&ids='+ str(detail_id) +'')
    if resp_latest.status_code == 200:
        resp_latest_json = json.loads(resp_latest.text, encoding='utf-8')
        if len(resp_latest_json.get('list')) == 0:
            return 'id error'
        video = {
            'type_id': resp_latest_json.get('list')[0].get('type_id'),
            'type_name': resp_latest_json.get('list')[0].get('type_name'),
            'vod_id': resp_latest_json.get('list')[0].get('vod_id'),
            'vod_name': resp_latest_json.get('list')[0].get('vod_name'),
            'vod_tag': resp_latest_json.get('list')[0].get('vod_tag'),
            'vod_pic': resp_latest_json.get('list')[0].get('vod_pic'),
            'vod_time': resp_latest_json.get('list')[0].get('vod_time'),
            'vod_play_url': resp_latest_json.get('list')[0].get('vod_play_url').split('$')[1]
        }
        context['video'] = video
    context['title'] = context['video']['vod_name']+"_"+context['title']
    context['keywords'] = context['video']['vod_name']+"_"+context['keywords']
    context['description'] = context['video']['vod_name']+","+context['description']
    # print("context = ", context)
    return render_template('/detail.html', context=context)

# 速度过慢可能抛弃
# @app.route('/', methods=['GET'])
# def index():
#     resp = requests.get('https://shayuapi.com/api.php/provide/vod/at/json/')
#     context = {
#         'title':'',
#         'keywords':'',
#         'description':'',
#         'baidu_code':'',
#         'kinds': [],  # 其中元素：{‘id’:***, 'text':***,'class_details_20':[{***},{***}]}
#     }
#     if resp.status_code == 200:
#         print(type(resp.text))
#         # print(resp.text.decode(encoding='UTF-8'))
#         # print(json.loads(resp.text, encoding='utf-8'))
#         resp_json = json.loads(resp.text, encoding='utf-8')
#         print(type(resp_json))
#         for temp in resp_json.get('class'):
#             print(temp)
#             print(type(temp))
#             kind = {
#                 'id':'',
#                 'text':'',
#                 'kind_details_20':[]
#             }
#             print(temp.get('id'))
#             kind['id'] = temp.get('type_id')
#             kind['text'] = temp.get('type_name')
#             detail_resp = requests.get('https://shayuapi.com/api.php/provide/vod/at/json?ac=detail&t=' + str(temp.get('type_id')))
#             detail_resp_json = json.loads(detail_resp.text, encoding='utf-8')
#             for detail in detail_resp_json.get('list'):
#                 list = {
#                     'type_id':detail.get('type_id'),
#                     'type_name': detail.get('type_name'),
#                     'vod_name': detail.get('vod_name'),
#                     'vod_pic': detail.get('vod_pic'),
#                     'vod_play_url': detail.get('vod_play_url'),
#                     'vod_tag': detail.get('vod_tag'),
#                     'vod_time': detail.get('vod_time')
#                 }
#                 kind['kind_details_20'].append(list)
#             context['kinds'].append(kind)
#         return context
#     return 'Hello Flask'

@app.route('/test', methods=['get'])
def test():
    return render_template('/detail.html')



def get_infos_from_database_by_url(url):
    print(url)
    regular = '[^http: |^https:][//](.*?)[/]$'
    res = re.findall(regular, url)
    res1 = '180.97.220.27:9393'
    if res:
        res1 = res[0]
    else:
        res1 = '180.97.220.27:9393'
    web_infos = WebsiteInfos.query.filter_by(url=res1).first()
    print("in function: web_infos = ", web_infos)
    contact_infos = ContactInfos.query.all()
    print("in function: contact_infos = ", contact_infos)
    ads_top_infos = AdsInfos.query.filter_by(ads_kind=1).all()
    print("in function: ads_top_infos = ", ads_top_infos)
    ads_bottom_infos = AdsInfos.query.filter_by(ads_kind=2).all()
    print("in function: ads_bottom_infos = ", ads_bottom_infos)
    ads_left_right_infos = AdsInfos.query.filter_by(ads_kind=3).all()
    print("in function: ads_left_right_infos = ", ads_left_right_infos)
    ads_top_bottom_infos = AdsInfos.query.filter_by(ads_kind=4).all()
    print("in function: ads_top_bottom_infos = ", ads_top_bottom_infos)
    infos = {
        'web_infos':web_infos,
        'contact_infos':contact_infos,
        'ads_top_infos':ads_top_infos,
        'ads_bottom_infos':ads_bottom_infos,
        'ads_left_right_infos':ads_left_right_infos,
        'ads_top_bottom_infos':ads_top_bottom_infos
    }
    return infos



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9393, debug=True)

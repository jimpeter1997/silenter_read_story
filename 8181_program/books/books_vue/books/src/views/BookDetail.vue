<template>
<div id="BookDetail">
    <Header />
    <Ads />
    <b-container v-if="items.detailsItems.length == 1">
        <b-row class="mt-3">
            <b-col>
            当前路径: <a href="/">首页</a>--<a :href="'/book/'+ items.detailsItems[0].book_id">{{ items.detailsItems[0].book_name }}</a>--{{items.detailsItems[0].detail_title}}
            </b-col>
        </b-row>
        <b-row class="mt-3 mb-3">
            <b-col id="book-detail-title" >
            {{ items.detailsItems[0].detail_title }}
            </b-col>
        </b-row>
        <b-row class="mb-3">

            <b-col class="normal-center " cols="4" md="4"  v-if="items.detailsItems[0].before_sort_id == ''">
                <a :href="'/book/'+ items.detailsItems[0].book_id ">上一页</a>
            </b-col>
            <b-col class="normal-center" cols="4" md="4"  v-else>
                <a :href="'/book/'+ items.detailsItems[0].book_id +'/'+ items.detailsItems[0].before_sort_id">上一页</a>
            </b-col>


            <b-col class="normal-center" cols="4" md="4">
                <a :href="'/book/'+ items.detailsItems[0].book_id">返回目录</a>
            </b-col>

            <b-col class="normal-center" cols="4" md="4" v-if="items.detailsItems[0].next_sort_id == ''">
                <a :href="'/book/'+ items.detailsItems[0].book_id  ">下一页</a>
            </b-col>
            <b-col class="normal-center" cols="4" md="4" v-else>
                <a :href="'/book/'+ items.detailsItems[0].book_id +'/'+ items.detailsItems[0].next_sort_id">下一页</a>
            </b-col>

        </b-row>
        <b-row>
            <b-col >
            <p id="content-text" v-html="replacebr(items.detailsItems[0].detail_content)"></p>
            </b-col>
        </b-row>
        <b-row class="mb-3">

            <b-col class="normal-center" cols="4" md="4"  v-if="items.detailsItems[0].before_sort_id == ''">
                <a :href="'/book/'+ items.detailsItems[0].book_id ">上一页</a>
            </b-col>
            <b-col class="normal-center" cols="4" md="4"  v-else>
                <a :href="'/book/'+ items.detailsItems[0].book_id +'/'+ items.detailsItems[0].before_sort_id">上一页</a>
            </b-col>


            <b-col class="normal-center" cols="4" md="4">
                <a :href="'/book/'+ items.detailsItems[0].book_id">返回目录</a>
            </b-col>

            <b-col class="normal-center" cols="4" md="4" v-if="items.detailsItems[0].next_sort_id == ''">
                <a :href="'/book/'+ items.detailsItems[0].book_id  ">下一页</a>
            </b-col>
            <b-col class="normal-center" cols="4" md="4" v-else>
                <a :href="'/book/'+ items.detailsItems[0].book_id +'/'+ items.detailsItems[0].next_sort_id">下一页</a>
            </b-col>

        </b-row>
    </b-container>

    <b-container v-else>
        服务器正在拼命给您加载资源中... ...
    </b-container>
    <AdsFooter />
    <Footer />
    </div>
    
</template>

<style lang="scss" scoped>
#book-detail-title{
    text-align: center;
    font-size: 28px;
}
#content-text{
    line-height: 40px;
    font-size: 18px;
}
</style>

<script>
import Header from "../components/Header.vue";
import Footer from "../components/Footer.vue";
import AdsFooter from "../components/AdsFooter.vue";
import Ads from "../components/Ads.vue";
import { ref, reactive, onMounted } from "@vue/composition-api";
import { GetInfoPost } from "../apis/read.js";
import { replacebr } from "../utils/replaceBr.js"


export default {
    name:"BookDetail",
    components:{
        Header,
        Footer,
        AdsFooter,
        Ads
    },
    setup(props, context){
        const detailPramas = reactive({
            url: context.root.$route.path,
            key:''
        });

        const items = reactive({
            detailsItems:[]
        });   
        
        GetInfoPost(detailPramas).then(resp => {
                // console.log(resp.data);
                items.detailsItems = resp.data.data;

                const titlePramas = reactive({
                    url: '/title',
                    key: 'bookindex'
                });



                GetInfoPost(titlePramas).then(resp => {
                    document.title = items.detailsItems[0].detail_title+'_'+items.detailsItems[0].book_name +'_'+resp.data.data[0];
                    document.querySelector('meta[name="keywords"]').setAttribute("content", items.detailsItems[0].book_name +','+items.detailsItems[0].detail_title);
                    // 沧元图无弹窗,是作者我吃西红柿所著的玄幻小说类小说，本站提供无弹窗阅读环境
                    document.querySelector('meta[name="description"]').setAttribute("content", items.detailsItems[0].book_name +','+items.detailsItems[0].detail_title+resp.data.data[2]);
                });
        });


        onMounted(()=>{
            
        });
        return {
            items,
            replacebr
        }
    }
}
</script>
<template>
  <div class="home">
    <Header />

    <b-container>
      <b-carousel
        id="carousel-fade"
        style="text-shadow: 0px 0px 2px #000"
        fade
        indicators
        img-width="1024"
        img-height="480"
      >
        <a href="/dushi">
          <b-carousel-slide
          caption="茫茫人海，谁能同行：都市小说"
          :img-src="dushi"
        ></b-carousel-slide>
        </a>
        <a href="/xiuzhen">
        <b-carousel-slide
          caption="天地不仁，万物刍狗：修真小说"
          :img-src="wuxia"
        ></b-carousel-slide>
        </a>
        <a href="/yanqing">
        <b-carousel-slide
          caption="相爱相杀，痛虐单狗：言情小说"
          :img-src="yanqing"
        ></b-carousel-slide>
        </a>
      </b-carousel>
      </b-container>


      <b-container class="mt-3">
          <b-row>
            <b-col cols="12" md="3">
              <div class="main-ph">
                <div class="main-titile">玄幻奇幻小说排行榜</div>
                <div class="main-ul-li">
                  <ul class="main-ul">
                  <li><span class="s1">1</span><span class="s2"><a href="/book/43552">平平无奇大师兄</a></span></li>
                  <li><span class="s1">2</span><span class="s2"><a href="/book/23488">圣墟（圣虚）</a></span></li>
                  <li><span class="s1">3</span><span class="s2"><a href="/book/28183">永恒圣王</a></span></li>
                  <li><span class="s1">4</span><span class="s2"><a href="/book/46713">大梦主</a></span></li>
                  <li><span class="s1">5</span><span class="s2"><a href="/book/20513">人皇纪</a></span></li>
                  <li><span class="s1">6</span><span class="s2"><a href="/book/28051">纯阳剑尊</a></span></li>
                  <li><span class="s1">7</span><span class="s2"><a href="/book/29445">妖龙古帝</a></span></li>
                  <li><span class="s1">8</span><span class="s2"><a href="/book/43252">不灭霸体诀</a></span></li>
                  <li><span class="s1">9</span><span class="s2"><a href="/book/44873">牧龙师</a></span></li>
                  <li><span class="s1">10</span><span class="s2"><a href="/book/44222">旱魃神探</a></span></li>
                  <li><span class="s1">11</span><span class="s2"><a href="/book/45837">疯狂进化</a></span></li>
                  <li><span class="s1">12</span><span class="s2"><a href="/book/21552">武破九荒</a></span></li>
                  <li><span class="s1">13</span><span class="s2"><a href="/book/12305">万古神帝</a></span></li>
                  <li><span class="s1">14</span><span class="s2"><a href="/book/10026">逆天邪神</a></span></li>
                  <li><span class="s1">15</span><span class="s2"><a href="/book/46706">横推从拔刀开始</a></span></li>
                </ul>
                  </div>
              </div>
            </b-col>
            
            <b-col cols="12" md="3">
              <div class="main-ph">
                <div class="main-titile">武侠仙侠排行</div>
                <div class="main-ul-li">
                  <ul class="main-ul">
                  <li><span class="s1">1</span><span class="s2"><a href="/book/23613">最强反套路系统</a></span></li>
                  <li><span class="s1">2</span><span class="s2"><a href="/book/44499">御九天</a></span></li>
                  <li><span class="s1">3</span><span class="s2"><a href="/book/7562">遮天</a></span></li>
                  <li><span class="s1">4</span><span class="s2"><a href="/book/43615">我真不是仙二代</a></span></li>
                  <li><span class="s1">5</span><span class="s2"><a href="/book/8763">修罗武神（逆道战神）</a></span></li>
                  <li><span class="s1">6</span><span class="s2"><a href="/book/45027">千机殿</a></span></li>
                  <li><span class="s1">7</span><span class="s2"><a href="/book/21528">都市绝品仙医</a></span></li>
                  <li><span class="s1">8</span><span class="s2"><a href="/book/41972">我师兄实在太稳健了</a></span></li>
                  <li><span class="s1">9</span><span class="s2"><a href="/book/9273">符皇</a></span></li>
                  <li><span class="s1">10</span><span class="s2"><a href="/book/33122">都市最强修真学生</a></span></li>
                  <li><span class="s1">11</span><span class="s2"><a href="/book/29493">元龙</a></span></li>
                  <li><span class="s1">12</span><span class="s2"><a href="/book/33226">仙草供应商</a></span></li>
                  <li><span class="s1">13</span><span class="s2"><a href="/book/28051">纯阳剑尊</a></span></li>
                  <li><span class="s1">14</span><span class="s2"><a href="/book/39166">废柴逆天召唤师</a></span></li>
                  <li><span class="s1">15</span><span class="s2"><a href="/book/25453">丹师剑宗</a></span></li>
                </ul>
                  </div>
              </div>
            </b-col>

            
            <b-col cols="12" md="3">
              <div class="main-ph">
                <div class="main-titile">都市言情排行</div>
                <div class="main-ul-li">
                  <ul class="main-ul">
                  <li><span class="s1">1</span><span class="s2"><a href="/book/29436">神医凰后</a></span></li>
                  <li><span class="s1">2</span><span class="s2"><a href="/book/21517">我的绝色总裁老婆</a></span></li>
                  <li><span class="s1">3</span><span class="s2"><a href="/book/29834">重生八零锦绣军婚</a></span></li>
                  <li><span class="s1">4</span><span class="s2"><a href="/book/25095">邪王追妻</a></span></li>
                  <li><span class="s1">5</span><span class="s2"><a href="/book/12210">重生之商界大亨</a></span></li>
                  <li><span class="s1">6</span><span class="s2"><a href="/book/44060">万族之劫</a></span></li>
                  <li><span class="s1">7</span><span class="s2"><a href="/book/41638">农门婆婆的诰命之路</a></span></li>
                  <li><span class="s1">8</span><span class="s2"><a href="/book/25160">魅王宠妻：鬼医纨绔妃</a></span></li>
                  <li><span class="s1">9</span><span class="s2"><a href="/book/11112">最强狂兵</a></span></li>
                  <li><span class="s1">10</span><span class="s2"><a href="/book/29876">极品全能狂医</a></span></li>
                  <li><span class="s1">11</span><span class="s2"><a href="/book/27357">女神的最强高手</a></span></li>
                  <li><span class="s1">12</span><span class="s2"><a href="/book/41718">东宫藏娇</a></span></li>
                  <li><span class="s1">13</span><span class="s2"><a href="/book/39042">娇妻狠大牌</a></span></li>
                  <li><span class="s1">14</span><span class="s2"><a href="/book/11029">修真聊天群</a></span></li>
                  <li><span class="s1">15</span><span class="s2"><a href="/book/26659">鉴宝金瞳</a></span></li>
                </ul>
                  </div>
              </div>
            </b-col>


            <b-col cols="12" md="3">
              <div class="main-ph">
                <div class="main-titile">历史军事排行</div>
                <div class="main-ul-li">
                  <ul class="main-ul">
                  <li><span class="s1">1</span><span class="s2"><a href="/book/43438">庶族无名</a></span></li>
                  <li><span class="s1">2</span><span class="s2"><a href="/book/43668">数风流人物</a></span></li>
                  <li><span class="s1">3</span><span class="s2"><a href="/book/25458">特种奶爸俏老婆</a></span></li>
                  <li><span class="s1">4</span><span class="s2"><a href="/book/29749">东晋北府一丘八</a></span></li>
                  <li><span class="s1">5</span><span class="s2"><a href="/book/43595">孤岛谍战</a></span></li>
                  <li><span class="s1">6</span><span class="s2"><a href="/book/28380">我在明朝当国公</a></span></li>
                  <li><span class="s1">7</span><span class="s2"><a href="/book/32611">明朝败家子</a></span></li>
                  <li><span class="s1">8</span><span class="s2"><a href="/book/8178">三国重生马孟起</a></span></li>
                  <li><span class="s1">9</span><span class="s2"><a href="/book/41865">都市医武狂龙</a></span></li>
                  <li><span class="s1">10</span><span class="s2"><a href="/book/11566">重生之苍莽人生</a></span></li>
                  <li><span class="s1">11</span><span class="s2"><a href="/book/24239">五代梦</a></span></li>
                  <li><span class="s1">12</span><span class="s2"><a href="/book/16937">重生之大涅磐</a></span></li>
                  <li><span class="s1">13</span><span class="s2"><a href="/book/28121">盛唐风华</a></span></li>
                  <li><span class="s1">14</span><span class="s2"><a href="/book/28735">长生九万年</a></span></li>
                  <li><span class="s1">15</span><span class="s2"><a href="/book/20227">女总裁的全能兵王</a></span></li>
                </ul>
                  </div>
              </div>
            </b-col>
          </b-row>

          <b-row>
            <b-col cols="12" md="3">
              <div class="main-ph">
                <div class="main-titile">科幻灵异排行</div>
                <div class="main-ul-li">
                  <ul class="main-ul">
                  <li><span class="s1">1</span><span class="s2"><a href="/book/32370">绝品神医</a></span></li>
                  <li><span class="s1">2</span><span class="s2"><a href="/book/13084">御鬼者传奇</a></span></li>
                  <li><span class="s1">3</span><span class="s2"><a href="/book/44145">超品命师</a></span></li>
                  <li><span class="s1">4</span><span class="s2"><a href="/book/43437">盖世双谐</a></span></li>
                  <li><span class="s1">5</span><span class="s2"><a href="/book/45433">诸天福运</a></span></li>
                  <li><span class="s1">6</span><span class="s2"><a href="/book/32466">星临诸天</a></span></li>
                  <li><span class="s1">7</span><span class="s2"><a href="/book/47802">我在绝地求生捡碎片</a></span></li>
                  <li><span class="s1">8</span><span class="s2"><a href="/book/13371">末日轮盘</a></span></li>
                  <li><span class="s1">9</span><span class="s2"><a href="/book/8357">进化的四十六亿重奏</a></span></li>
                  <li><span class="s1">10</span><span class="s2"><a href="/book/40230">真实末日游戏</a></span></li>
                  <li><span class="s1">11</span><span class="s2"><a href="/book/31822">学霸的黑科技系统</a></span></li>
                  <li><span class="s1">12</span><span class="s2"><a href="/book/41913">科技之全球垄断</a></span></li>
                  <li><span class="s1">13</span><span class="s2"><a href="/book/29267">极品捉鬼系统</a></span></li>
                  <li><span class="s1">14</span><span class="s2"><a href="/book/21562">劫天运（鬼姐姐）</a></span></li>
                  <li><span class="s1">15</span><span class="s2"><a href="/book/32245">通灵实录</a></span></li>
                </ul>
                  </div>
              </div>
            </b-col>

            <b-col cols="12" md="3">
              <div class="main-ph">
                <div class="main-titile">网游竞技排行</div>
                <div class="main-ul-li">
                  <ul class="main-ul">
                  <li><span class="s1">1</span><span class="s2"><a href="/book/29105">超神机械师</a></span></li>
                  <li><span class="s1">2</span><span class="s2"><a href="/book/32312">王者时刻</a></span></li>
                  <li><span class="s1">3</span><span class="s2"><a href="/book/29140">海贼之疾风剑豪</a></span></li>
                  <li><span class="s1">4</span><span class="s2"><a href="/book/44392">轮回大劫主</a></span></li>
                  <li><span class="s1">5</span><span class="s2"><a href="/book/7589">网游之天下无双</a></span></li>
                  <li><span class="s1">6</span><span class="s2"><a href="/book/46139">文明之万界领主</a></span></li>
                  <li><span class="s1">7</span><span class="s2"><a href="/book/22487">lol之电竞天王</a></span></li>
                  <li><span class="s1">8</span><span class="s2"><a href="/book/7567">全职高手</a></span></li>
                  <li><span class="s1">9</span><span class="s2"><a href="/book/9389">暗黑破坏神之毁灭</a></span></li>
                  <li><span class="s1">10</span><span class="s2"><a href="/book/7815">网游之天谴修罗</a></span></li>
                  <li><span class="s1">11</span><span class="s2"><a href="/book/11216">重生之最强剑神</a></span></li>
                  <li><span class="s1">12</span><span class="s2"><a href="/book/22608">在地下城行走的人果然不正常</a></span></li>
                  <li><span class="s1">13</span><span class="s2"><a href="/book/44047">峡谷之巅</a></span></li>
                  <li><span class="s1">14</span><span class="s2"><a href="/book/41990">穿越火线之英雄有梦</a></span></li>
                  <li><span class="s1">15</span><span class="s2"><a href="/book/31044">游戏之狩魔猎人</a></span></li>
                </ul>
                  </div>
              </div>
            </b-col>

            <b-col cols="12" md="3">
              <div class="main-ph">
                <div class="main-titile">女生频道排行</div>
                <div class="main-ul-li">
                  <ul class="main-ul">
                  <li><span class="s1">1</span><span class="s2"><a href="/book/29436">神医凰后</a></span></li>
                  <li><span class="s1">2</span><span class="s2"><a href="/book/29834">重生八零锦绣军婚</a></span></li>
                  <li><span class="s1">3</span><span class="s2"><a href="/book/28150">帝少心头宠</a></span></li>
                  <li><span class="s1">4</span><span class="s2"><a href="/book/25058">嫡女重生记</a></span></li>
                  <li><span class="s1">5</span><span class="s2"><a href="/book/25625">锦绣重生</a></span></li>
                  <li><span class="s1">6</span><span class="s2"><a href="/book/25103">绝世神医：腹黑大小姐</a></span></li>
                  <li><span class="s1">7</span><span class="s2"><a href="/book/41934">天作不合</a></span></li>
                  <li><span class="s1">8</span><span class="s2"><a href="/book/18006">恋爱高手</a></span></li>
                  <li><span class="s1">9</span><span class="s2"><a href="/book/46946">娘子万安</a></span></li>
                  <li><span class="s1">10</span><span class="s2"><a href="/book/41348">嫁偶天成</a></span></li>
                  <li><span class="s1">11</span><span class="s2"><a href="/book/40751">巫女的时空旅行</a></span></li>
                  <li><span class="s1">12</span><span class="s2"><a href="/book/41940">锦鲤王妃有空间</a></span></li>
                  <li><span class="s1">13</span><span class="s2"><a href="/book/41771">暖君</a></span></li>
                  <li><span class="s1">14</span><span class="s2"><a href="/book/17785">家里养个狐狸精</a></span></li>
                  <li><span class="s1">15</span><span class="s2"><a href="/book/39061">至尊瞳术师</a></span></li>
                </ul>
                  </div>
              </div>
            </b-col>

            <b-col cols="12" md="3">
              <div class="main-ph">
                <div class="main-titile">完本小说排行</div>
                <div class="main-ul-li">
                  <ul class="main-ul">
                  <li><span class="s1">1</span><span class="s2"><a href="/book/7718">雪中悍刀行</a></span></li>
                  <li><span class="s1">2</span><span class="s2"><a href="/book/13406">纯阳战神</a></span></li>
                  <li><span class="s1">3</span><span class="s2"><a href="/book/9175">守望黎明号</a></span></li>
                  <li><span class="s1">4</span><span class="s2"><a href="/book/14745">异界海盗王</a></span></li>
                  <li><span class="s1">5</span><span class="s2"><a href="/book/8349">锻仙</a></span></li>
                  <li><span class="s1">6</span><span class="s2"><a href="/book/7562">遮天</a></span></li>
                  <li><span class="s1">7</span><span class="s2"><a href="/book/12051">超品透视</a></span></li>
                  <li><span class="s1">8</span><span class="s2"><a href="/book/21197">寒门首辅</a></span></li>
                  <li><span class="s1">9</span><span class="s2"><a href="/book/25058">嫡女重生记</a></span></li>
                  <li><span class="s1">10</span><span class="s2"><a href="/book/7825">我的美女老师</a></span></li>
                  <li><span class="s1">11</span><span class="s2"><a href="/book/10926">哥几个，走着</a></span></li>
                  <li><span class="s1">12</span><span class="s2"><a href="/book/10483">执掌乾坤</a></span></li>
                  <li><span class="s1">13</span><span class="s2"><a href="/book/21535">特种兵之利刃</a></span></li>
                  <li><span class="s1">14</span><span class="s2"><a href="/book/9177">官道无疆</a></span></li>
                  <li><span class="s1">15</span><span class="s2"><a href="/book/9083">武道至尊</a></span></li>
                </ul>
                  </div>
              </div>
            </b-col>



          </b-row>
      </b-container>


    <Footer />


  </div>


</template>

<style lang="scss" scoped>
.main-ph{
    width: 100%;
    margin-right: 4px;
    margin-bottom: 10px;
    float: left;
    padding-bottom: 0;
    border: 2px solid #88C6E5;
    overflow: hidden;
    padding: 0 0 0px;
    box-sizing: border-box;
    background: #FEF9EF;
}
.main-titile{
    background-color: #E1ECED;
    border-bottom: 1px solid #88C6E5;
    font-size: 14px;
    font-weight: 700;
    height: 32px;
    line-height: 32px;
    overflow: hidden;
    margin: 0;
    padding: 0 10px;
    box-sizing: border-box;
}
.main-ul-li{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
.main-ul{
  padding: 4px 10px;
  list-style: none;
  margin: 0;
  box-sizing: border-box;
  margin-block-start: 1em;
    margin-block-end: 1em;
    margin-inline-start: 0px;
    margin-inline-end: 0px;
    padding-inline-start: 40px;
}
.main-ul li{
  border-bottom: 0 none;
  height: 32px;
  line-height: 32px;
  overflow: hidden;
  display: list-item;
    text-align: -webkit-match-parent;
        margin: 0;
    padding: 0;
    box-sizing: border-box;
}

.s1{
  max-width: 26px;
    font-style: italic;
    color: #999;
    font-family: "Verdana";
    width: 60px;
        float: left;
}
.s2{
  width: 142px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
        float: left;
}
.s2 a{
  color: #6F78A7;
  text-decoration: none;
    outline: none;
    -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}
</style>

<script>
import Header from "../components/Header.vue";
import Footer from "../components/Footer.vue";
import { GetInfoPost } from "../apis/read.js";
import { ref, reactive, onMounted } from "@vue/composition-api";
import dushi from "../assets/images/dushi.jpg";
import wuxia from "../assets/images/wuxia.jpeg";
import yanqing from "../assets/images/yanqing.jpeg";


export default {
  name: "Home",
  components: {
    Header,
    Footer
  },
  setup(props, context){

    const titlePramas = reactive({
      url: '/title',
      key: 'index'
    });



    GetInfoPost(titlePramas).then(resp => {
      // console.log("In Home title = ", resp.data.data);
      document.title = resp.data.data[0];
      document.querySelector('meta[name="keywords"]').setAttribute("content", resp.data.data[1]);
      document.querySelector('meta[name="description"]').setAttribute("content", resp.data.data[2]);
    });


    // document.title = '风华绝代的alexhunter';
    // document.querySelector('meta[name="keywords"]').setAttribute("content", "风华绝代的keywords");
    // document.querySelector('meta[name="description"]').setAttribute("content", "风华绝代的description");
    

    

    onMounted(()=>{
      // console.log(context.root.$route.path)
    });


    return {
      dushi,
      wuxia,
      yanqing
    }
  }

};
</script>
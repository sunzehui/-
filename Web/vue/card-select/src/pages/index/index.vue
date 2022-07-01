<template>
  <view class="content">
    <view class="card">
      <h2>已选频道</h2>
      <draggable
        class="selected"
        tag="view"
        v-model="selected"
        v-bind="dragOptions"
      >
        <transition-group type="transition">
          <view class="item" v-for="item in selected" :key="item.id">
            <view class="img">
              <img :src="item.img" :alt="item.title" srcset="" />
            </view>
            <span>{{ item.title }}</span>
            <view class="btn-group">
              <button @click="removeChannelItem(item)">del</button>
              <button>三</button>
            </view>
          </view>
        </transition-group>
      </draggable>
      <h2>频道列表</h2>
      <view class="unselect">
        <view class="item" v-for="item in unselect" :key="item.title">
          <view class="img">
            <img :src="item.img" :alt="item.title" srcset="" />
          </view>
          <span>{{ item.title }}</span>
          <view class="btn-group">
            <button @click="addChannelItem(item)">add</button>
          </view>
        </view>
      </view>
    </view>
  </view>
</template>

<script lang="ts">
import Vue from "vue";
import deepCopy from "lodash/cloneDeep";
import draggable from "vuedraggable";
import { Component } from "vue-property-decorator";
type Channel = Record<"img" | "title" | "id", string>;

@Component({
  name: "index",
  components: { draggable },
})
export default class Index extends Vue {
  unselect = [] as Channel[];
  selected = [] as Channel[];
  channelList = [] as Channel[];
  drag = false;
  get dragOptions() {
    return {
      animation: 200,
    };
  }
  onLoad() {
    this.channelList = [
      { img: "http://via.placeholder.com/640x360", title: "百里守约", id: "1" },
      { img: "http://via.placeholder.com/640x360", title: "雅典娜", id: "2" },
      { img: "http://via.placeholder.com/640x360", title: "东皇太一", id: "3" },
    ];
    this.unselect = deepCopy(this.channelList);
  }
  addChannelItem(channel: Channel) {
    this.selected.push(channel);
    // find and remove
    const itemInUnselectIdx = this.unselect.findIndex(
      (item) => item.title === channel.title
    );
    this.unselect.splice(itemInUnselectIdx, 1);
  }
  removeChannelItem(channel: Channel) {
    // find and remove
    const itemInSelectedIdx = this.selected.findIndex(
      (item) => item.title === channel.title
    );
    this.selected.splice(itemInSelectedIdx, 1);
    this.unselect.push(channel);
  }
}
</script>

<style lang="less">
.content {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.card {
  width: 100%;
  height: 100%;
  padding: 0 30px;
  box-sizing: border-box;
  .item {
    width: 100%;
    height: 80px;
    padding: 10px 0;
    display: flex;
    gap: 20px;
    box-sizing: border-box;
    align-items: center;
    .img {
      height: 100%;
      width: 80px;

      img {
        height: 100%;
        width: 100%;
        object-fit: cover;
      }
    }
    .btn-group {
      margin-left: auto;
      display: flex;
      gap: 20px;
    }
  }
  .selected {
  }
}
</style>

<template>
  <div class="home">
     <Aside />
     <div class="p-4 bg-white mt-6 mr-6 pb-6 sm:ml-64 rounded-lg">
       
        <div class="flex">
          <div class="w-1/3 border-r border-gray-300">
              <div class="flex justify-between  pb-2">
                <h3 class="font-bold font-rope text-lg">History</h3>
              </div>
              
             <div class="mt-4 font-rope relative w-full">
                  <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
                      <svg aria-hidden="true" class="w-5 h-5 text-[#2a2732]" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z" clip-rule="evenodd"></path></svg>
                  </div>
                  <input type="text"  class="bg-white text-xs border border-gray-300 text-[#2a2732] text-sm rounded focus:ring-0 focus:outline-none block w-72 pl-10 p-2.5  placeholder-[#2a2732]" placeholder="Search messages" required>
              </div>
             
              
             <div>
                <div v-for="chat of previousChats " class="mt-4 bg-[#f4f6f8]/40 transition-colors duration-300 hover:bg-white hover:shadow font-rope flex p-3 mr-4 rounded-lg cursor-pointer">
                 <img class="h-10 w-10 rounded-full object-cover" src="../assets/WhatsApp Image 2023-04-02 at 19.44.10.jpeg" alt="">
                   <div class="ml-4">
                      <div class="flex font-bold font-rope justify-between"><h3>Nick</h3></div>
                      <p class="text-gray-600 text-xs">{{ chat.value }}</p>
                   </div>
                </div>
                
    
             </div>
              
           </div>
           <div class="ml-4  w-2/3 flex flex-col h-full">
              <div class="font-rope flex pb-6 justify-between">
                <div class="flex">
                   <img class="h-10 w-10 rounded-full object-cover" src="../assets/WhatsApp Image 2023-04-02 at 19.44.10.jpeg" alt="">
                  
                </div>
                 <select v-model="selected_datastore" class="bg-white mr-4 border border-gray-300 text-[#2a2732] text-xs rounded focus:ring-0 focus:outline-none block w-64 p-2">
                    <option value="">Choose a datastore to query</option>
                    <option v-for="doc of documents" :value="doc.name">{{doc.name}}</option>
                    
                 </select>
              </div>
              
              <div v-if="filteredChats.length == 0" class="mt-6 overflow-y-auto pb-4 font-rope">
                  <div v-for="chat of storedChats">
                  <div v-if="chat.type == 'prompt'" class="mr-4 flex justify-end">
                    <div  class="px-5 mb-2 bg-[#010918] 33354a text-sm text-white py-3 text-sm max-w-[50%] rounded">
                       <p>
                          {{ chat.value }}
                       </p>
                    </div>
                 </div>
                 <div v-if="chat.type == 'response'" class="relative  flex justify-start">
                    <div class="px-5 mb-2 bg-[#f2f4f6]/40 py-3 text-sm max-w-[50%] rounded-lg">
                       <i class="fa fa-caret-up text-violet-400 -top-2 absolute" ></i>
                       <p class="text-start ml-2">{{ chat.value }}</p>
                    </div>
                 </div>
                  </div>
                 
              </div>
              <div v-else class="overflow-y-auto mt-6 pb-4 font-rope">
                  <div v-for="chat of filteredChats">
                  <div v-if="chat.type == 'prompt'" class="mr-4 flex justify-end">
                    <div  class="px-5 mb-2 bg-[#010918] 33354a text-sm text-white py-3 text-sm max-w-[50%] rounded">
                       <p>
                          {{ chat.value }}
                       </p>
                    </div>
                 </div>
                 <div v-if="chat.type == 'response'" class="relative  flex justify-start">
                    <div class="px-5 mb-2 bg-[#f2f4f6]/40 py-3 text-sm max-w-[50%] rounded-lg">
                       <i class="fa fa-caret-up text-violet-400 -top-2 absolute" ></i>
                       <p class="text-start ml-2">{{ chat.value }}</p>
                    </div>
                 </div>
                  </div>
                 
              </div>
              <!--  -->
              <div class="mr-4">
                 <form>
                    <div class="flex items-center px-3 py-2 rounded-lg bg-[#f3f2f2]">
                       <button type="button" class="inline-flex justify-center p-2 text-[#2a2732] rounded-lg cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600">
                          <svg aria-hidden="true" class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                             <path fill-rule="evenodd" d="M4 3a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V5a2 2 0 00-2-2H4zm12 12H4l4-8 3 6 2-4 3 6z" clip-rule="evenodd"></path>
                          </svg>
                          <span class="sr-only">Upload image</span>
                       </button>

                       <textarea v-model="prompt" id="chat" rows="1" class="block font-rope mx-4 p-2.5 w-full text-sm placeholder:text-xs placeholder:text-[#2a2732] text-[#2a2732] bg-white rounded-lg focus:ring-0 focus:outline-none" placeholder="Ask me anything..."></textarea>
                       <button @click.prevent="sendPrompt" type="submit" class="inline-flex justify-center p-2 text-[#8b3dff] rounded-full cursor-pointer hover:bg-purple-100">
                          <svg aria-hidden="true" class="w-6 h-6 rotate-90" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                             <path d="M10.894 2.553a1 1 0 00-1.788 0l-7 14a1 1 0 001.169 1.409l5-1.429A1 1 0 009 15.571V11a1 1 0 112 0v4.571a1 1 0 00.725.962l5 1.428a1 1 0 001.17-1.408l-7-14z"></path>
                          </svg>
                       </button>
                    </div>
                 </form>
              </div>

              
           </div>
           
        </div>
        
     </div>
  </div>
</template>
<script>
import Aside from '@/components/Aside.vue'
import axios from "axios"
export default {
  name: 'ChatView',
  components: {
    Aside
},
  data(){
    return {
      show_form: false,
      prompt: "",
      response: "",
      selected_datastore: "",
      responses: [],
      prompts: [],
      chats: [],
      documents: []
    }
  },
  computed: {
      filteredChats: function() {
          return this.chats.slice(-7)
      },
      storedChats: function() {
          return JSON.parse(localStorage.getItem("my_chats")).slice(-7)
      },
      previousChats: function() {
          return JSON.parse(localStorage.getItem("my_chats")).filter((chat) => {
        return chat.type.toLowerCase().includes('prompt');
    });
      }
  },
  methods: {
    toggleForm() {
      this.show_form = !this.show_form
    },
    getDocuments() {
    axios.get('http://localhost:8000/').then(res=>{
      this.documents = res.data.documents
     
    })
  },
    sendPrompt() {
      this.chats.push({"value": this.prompt, "type": "prompt"})

      axios.get(`http://localhost:8000/chat/?prompt=${this.prompt}&file=${this.selected_datastore}`).then(res=>{
          this.response = res.data.response
          this.chats.push({"value": res.data.response, "type": "response"})
          localStorage.setItem('my_chats', JSON.stringify(this.chats))
      })
    }
  },
  mounted() {
      this.getDocuments()
  }
}
</script>
<style>
html {
    background-color: #f3f2f2;
}
/* 080c0f */
</style>
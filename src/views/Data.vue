<template>
    <div>
       <Aside />
       <div v-if="showModal" class="overflow-x-hidden overflow-y-auto fixed inset-0 z-50 outline-none focus:outline-none justify-center items-center flex">
          <div class="relative w-full max-w-md max-h-full">
             <!-- Modal content -->
             <div class="relative bg-white rounded-lg shadow">
                <button @click="toggleModal()" type="button" class="absolute top-3 right-2.5 text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center" data-modal-hide="authentication-modal">
                   <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                      <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path>
                   </svg>
                   <span class="sr-only">Close modal</span>
                </button>
                <div class="px-6 py-6 lg:px-8">
                   <h3 class="mb-4 text-xl font-bold font-rope text-[#2a2732]">Upload a file</h3>
                   <form class="space-y-6 font-rope" >
                      <div>
                         <label  class="block text-[#2a2732] mb-2 text-sm font-rope font-medium text-start">Type</label>
                         <select v-model="file_type" class="bg-white text-[#2a2732] border border-gray-300 text-gray-900 text-sm rounded focus:ring-0 focus:outline-none block w-full p-2.5">
                            <option value="">Choose file type</option>
                            <option value="json">JSON</option>
                            <option value="pdf">PDF</option>
                            <option value="word">DOCX</option>
                         </select>
                      </div>
                      <div class="flex items-center justify-center w-full">
                         <label for="dropzone-file" class="flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-white hover:bg-[#40576d12]">
                            <div class="flex flex-col items-center font-rope justify-center pt-5 pb-6">
                               <svg aria-hidden="true" class="w-10 h-10 mb-3 text-[#2a2732]" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"></path>
                               </svg>
                               <p class="mb-2 text-sm text-[#2a2732]"><span class="font-semibold">Click to upload</span> or drag and drop</p>
                               <p class="text-xs text-[#2a2732]">PDF, DOCX, PPTX, CSV, JSON</p>
                            </div>
                            <input id="dropzone-file" @change="handleFileUpload( $event )" type="file" class="hidden" />
                         </label>
                      </div>
                      <button @click.prevent="submitFile" type="submit" class="w-full text-white bg-[#8b3dff] font-medium rounded-lg text-sm px-5 py-2.5 text-center">Proceed</button>
                   </form>
                </div>
             </div>
          </div>
       </div>
       <div v-if="showModal" class="opacity-25 fixed inset-0 z-40 bg-black"></div>
       <div class="p-4 font-rope bg-white mt-4 mr-4 pb-32 sm:ml-72 rounded">

        

          <div class="flex mt-4 justify-between">
             <form class="flex items-center">
                <label for="simple-search" class="sr-only">Search</label>
                <div class="relative w-full">
                   <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
                      <svg aria-hidden="true" class="w-5 h-5 text-[#2a2732]" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                         <path fill-rule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z" clip-rule="evenodd"></path>
                      </svg>
                   </div>
                   <input type="text" id="simple-search" class="bg-white border border-gray-300 text-[#2a2732] text-sm rounded focus:ring-0 focus:outline-none block w-72 pl-10 p-2.5  placeholder:text-xs placeholder-[#2a2732]" placeholder="Search your documents" required>
                </div>
             </form>
             <div v-if="success" class="flex items-center w-72 max-w-xs p-1 text-emerald-600 bg-emerald-100 border border-emerald-300 rounded shadow " role="alert">
            <div class="inline-flex items-center justify-center flex-shrink-0 w-8 h-8 text-emerald-600 bg-emerald-100 rounded">
                <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path></svg>
                <span class="sr-only">Check icon</span>
            </div>
            <div class="ml-3 text-sm font-normal">File added successfully!</div>
            <button @click="success = !success" type="button" class="ml-auto -mx-0.5 -my-1.5 bg-emerald-100 text-emerald-400 hover:text-emerald-900 rounded focus:ring-0 p-1.5 hover:bg-emerald-100 inline-flex h-8 w-8"  aria-label="Close">
                <span class="sr-only">Close</span>
                <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
            </button>
        </div>
             <button @click="toggleModal()"  class="bg-[#8b3dff] text-white px-4  rounded">Upload Document</button>
          </div>
          <div class="relative font-rope overflow-x-auto mt-12">
             <table class="w-full text-sm text-left text-gray-500">
                <thead class="text-xs text-[#2a2732] uppercase bg-[#40576d12] font-bold">
                   <tr>
                      <th scope="col" class="px-6 py-3">
                         name
                      </th>
                      <th scope="col" class="px-6 py-3">
                         type
                      </th>
                      <th scope="col" class="px-6 py-3">
                         uploaded on
                      </th>
                      <th scope="col" class="px-6 py-3">
                         Action
                      </th>
                      <th scope="col" class="px-12 py-3">
                         Extra Action
                      </th>
                   </tr>
                </thead>
                <tbody>
                   <tr v-for="document of documents" class="bg-white font-rope text-[#2a2732] border-b">
                      <th scope="row" class="px-6 py-4 font-medium  whitespace-nowrap">
                         {{ document.name }}
                      </th>
                      <td class="px-6 py-4"> 
                         {{ document.type.toUpperCase() }}
                      </td>
                      <td class="px-6 py-4">
                         {{ formatDate(document.created) }}
                      </td>
                      <td class="px-6 py-4">
                         <button class="bg-[#8b3dff] text-white px-3 py-0.5 rounded">Select</button>
                      </td>
                      <td class=" py-4 flex gap-4">
                         <button class="bg-[#40576d12] 3a3b4d text-gray-800 px-3 py-0.5 rounded">Download</button>
                         <button class="bg-[#040406] 3a3b4d text-white px-3 py-0.5 rounded">Remove</button>
                      </td>
                   </tr>
                </tbody>
             </table>
          </div>
       </div>
    </div>
</template>

<script>
import Aside from '@/components/Aside.vue'
import moment from 'moment'
import axios from "axios"
export default {
    name: 'DataView',
    components: {
        Aside
    },
    data(){
      return {
        show_form: false,
        file: '',
        file_type: '',
        documents: [],
        showModal: false,
        success: true
      }
    },
    methods: {
        toggleModal () {
            this.showModal = !this.showModal;
        },
    
        handleFileUpload( event ){
            this.file = event.target.files[0];
        },
        submitFile(){
            let formData = new FormData();
            formData.append('type', this.file_type);
            formData.append('file', this.file, this.file.name);
            formData.append('name', this.file.name);
        
            axios.post( 'http://localhost:8000/',
            formData,
            {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            }
            ).then(res=>{
                console.log(res)
                this.toggleModal()
                this.getDocuments()
            })
            .catch(error=>{
                console.log(error)
            })
        },
  
        getDocuments() {
            axios.get('http://localhost:8000/').then(res=>{
            this.documents = res.data.documents
            console.log(this.documents)
            })
        },

        formatDate(date) {
            return moment(date, 'YYYY-MM-DD').format('DD-MM-YYYY')
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
</style>
<template>
  <div>
     <nav class="bg-[#010918] p-3  w-full">
        <div class="flex mt-2 justify-between">
           <div class="flex gap-1">
              <img class="h-16 w-16 -mt-4 rounded-full object-cover" src="../assets/logo.webp" alt="">
              <h3 class="text-white font-rose font-bold text-2xl">Iris</h3>
           </div>
           <ul class="font-rope inline-flex gap-8">
              <li class="text-white font-bold hover:text-purple-500 rounded-lg transition-colors duration-300 cursor-pointer">Features</li>
              <!-- <li class="text-white font-bold hover:text-purple-500 rounded-lg transition-colors duration-300 cursor-pointer">Docs</li> -->
              <li class="text-white font-bold hover:text-purple-500 rounded-lg transition-colors duration-300 cursor-pointer">How It Works</li>
              <li class="text-white font-bold hover:text-purple-500 rounded-lg transition-colors duration-300 cursor-pointer">Pricing</li>
              <!-- <li class="text-white font-bold hover:text-purple-500 rounded-lg transition-colors duration-300 cursor-pointer">Contact</li> -->
           </ul>
           <div class="-mt-1">
              <button class="bg-[#8b3dff] [#f2f292] px-6 py-2 font-rope font-bold rounded text-white transition-colors duration-300 cursor-pointer">
              Try Free
              </button>
           </div>
        </div>
     </nav>
  
  <div class="container mx-auto pb-6">
     
     <div class="mt-32 grid grid-cols-2 gap-x-12">
        <div class="">
           <h2 class="font-rope font-bold text-start text-gray-800 text-4xl">Build context-aware AI agent  <br> <span class="">trained on your own custom data.</span> </h2>
           <p class="mt-6 text-start font-rope text-[#040406]">Our no-code platform allows you to upload your predefined data <br> and provides an interface for you to ask questions based on that data.</p>
           <div class="mt-20 font-rope flex gap-x-8">
              <button class="bg-[#010918] px-6 py-2 rounded text-white transition-colors duration-300 cursor-pointer">
              Sign up
              </button>
              <button class="bg-[#8b3dff] px-6 py-2 rounded text-white transition-colors duration-300 cursor-pointer">
              Book demo
              </button>
           </div>
        </div>
        <div>
           <img class="rounded-lg" src="../assets/Screenshot 2023-05-13 at 10.23.07.png" alt="">
        </div>
     </div>
     <div id="get_started" class="mt-32">
      <h2 class="text-start text-gray-800 font-bold font-rope text-3xl">Get started in<span class=""> 3 easy steps</span> </h2>
      <div class="grid font-rope text-gray-800 grid-cols-3 gap-x-12 mt-12">
          <div class="bg-white p-5 rounded-lg">
              <p class="ml-3 text-start">Upload predifined data</p>
              <p class="ml-3 text-xs text-start">This could be a csv, pdf, docx, pptx, txt, webpage that contains your data</p>

          </div>
          <div class="bg-white p-4 rounded-lg">
              <p class="ml-3 text-start">Select your data from the dropdown</p>
              <p class="ml-3 text-xs text-start">Effortlessly pick the data file you uploaded earlier to serve as context.</p>

          </div>
          <div class="bg-white p-4 rounded-lg">
              <p class="ml-3 text-start">Ask the agent questions!</p>
              <p class="ml-3 text-xs text-start">Go ahead and get answers to your questions, chat with the agent!</p>

          </div>
      </div>
           
     </div>
     <div class="mt-32 grid grid-cols-2 gap-x-12">
        <div class="">
           <h2 class="text-start text-[#040406] font-bold font-rope text-4xl">Try with your own data</h2>
           <p class="font-rope mt-6 text-start text-[#040406]/80">
              Upload a CSV and ask questions from it, <br>
              or ask questions on our predefined datasets.
           </p>
           <div class="mt-8 flex gap-x-8">
              <button class="bg-[#8b3dff] px-6 py-2 font-rope font-bold rounded text-white transition-colors duration-300 cursor-pointer">
              Upload CSV
              </button>
           </div>
        </div>
        <div>
           <div class="grid font-rope cursor-pointer grid-cols-3 gap-x-12">
              <div class="shadow h-16  transition-colors duration-300 rounded-lg bg-white">
                 <h3 class="text-[#040406]  mt-4 font-bold">DATA 1</h3>
              </div>
              <div class="shadow h-16 rounded-lg bg-white">
                 <h3 class="text-[#040406] mt-4 font-bold">DATA 2</h3>
              </div>
              <div class="shadow h-16 rounded-lg bg-white">
                 <h3 class="text-[#040406] mt-4 font-bold">DATA 3</h3>
              </div>

           </div>
           <div class="mt-4 font-rope">
              <p class="text-[#040406]/80 text-start">Note:
                 This data is about students and their academic performance. It includes the student's name, student ID, and their cumulative grade point average (CGPA).
              </p>
              <div class="flex mt-8 gap-4">
                 <input type="text" class="bg-white p-4 focus:ring-0 focus:outline-none text-[#040406] placeholder:text-[#040406] placeholder:text-xs w-full py-1.5 rounded-lg" placeholder="Ask me anything based on the data">
                 <button class="bg-[#8b3dff] font-rope px-6 py-2 rounded-lg text-white transition-colors duration-300 cursor-pointer">
                 Ask
                 </button>
              </div>
              <div class="mt-4 font-rope">
                 <h3 class="text-[#040406] text-start">Response from agent</h3>
                 <div  class="relative mt-2 flex justify-start">
                    <div class="px-5 mb-2 bg-white py-3 text-sm  rounded-lg">
                       
                       <p class="text-start font-rope ml-2">This data is about students and their academic performance. It includes the student's name, student ID, and their cumulative grade point average (CGPA).
                       </p>
                    </div>
                 </div>
              </div>
           </div>
        </div>
     </div>

     <div class="font-rope mt-32">
      <h2 class="text-start flex gap-2 text-[#040406] font-bold font-rope text-4xl">Experience AI like never before <span>
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-10 text-purple-500 h-10">
<path stroke-linecap="round" stroke-linejoin="round" d="M9.813 15.904L9 18.75l-.813-2.846a4.5 4.5 0 00-3.09-3.09L2.25 12l2.846-.813a4.5 4.5 0 003.09-3.09L9 5.25l.813 2.846a4.5 4.5 0 003.09 3.09L15.75 12l-2.846.813a4.5 4.5 0 00-3.09 3.09zM18.259 8.715L18 9.75l-.259-1.035a3.375 3.375 0 00-2.455-2.456L14.25 6l1.036-.259a3.375 3.375 0 002.455-2.456L18 2.25l.259 1.035a3.375 3.375 0 002.456 2.456L21.75 6l-1.035.259a3.375 3.375 0 00-2.456 2.456zM16.894 20.567L16.5 21.75l-.394-1.183a2.25 2.25 0 00-1.423-1.423L13.5 18.75l1.183-.394a2.25 2.25 0 001.423-1.423l.394-1.183.394 1.183a2.25 2.25 0 001.423 1.423l1.183.394-1.183.394a2.25 2.25 0 00-1.423 1.423z" />
</svg>

      </span></h2>
      <p class="text-start font-rope text-[#040406]/80 mt-2 text-xl">Our AI-powered agents provide a unique conversational experience that you won't find anywhere else.</p>
      <div class="grid font-primary grid-cols-3  text-[#040406] gap-x-12 gap-y-8 mt-8">
          <div class="bg-white font-rope  p-4 rounded-lg">
              <h4 class="ml-3 flex gap-2 justify-start font-bold items-end">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5 mb-0.5 text-green-500">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M20.25 8.511c.884.284 1.5 1.128 1.5 2.097v4.286c0 1.136-.847 2.1-1.98 2.193-.34.027-.68.052-1.02.072v3.091l-3-3c-1.354 0-2.694-.055-4.02-.163a2.115 2.115 0 01-.825-.242m9.345-8.334a2.126 2.126 0 00-.476-.095 48.64 48.64 0 00-8.048 0c-1.131.094-1.976 1.057-1.976 2.192v4.286c0 .837.46 1.58 1.155 1.951m9.345-8.334V6.637c0-1.621-1.152-3.026-2.76-3.235A48.455 48.455 0 0011.25 3c-2.115 0-4.198.137-6.24.402-1.608.209-2.76 1.614-2.76 3.235v6.226c0 1.621 1.152 3.026 2.76 3.235.577.075 1.157.14 1.74.194V21l4.155-4.155" />
                  </svg>

                  Real Conversations</h4>
              <p class="ml-3 mt-1 text-start">
                  Converse with agent based on your data entries, uploaded by you — as though your agent is actually human.
              </p>

          </div>
          <div class="bg-white font-rope  p-4 rounded-lg">
              <h4 class="ml-3 flex gap-2 justify-start font-bold items-end">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5 text-purple-500 mb-0.5">
<path stroke-linecap="round" stroke-linejoin="round" d="M8.25 6.75h12M8.25 12h12m-12 5.25h12M3.75 6.75h.007v.008H3.75V6.75zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0zM3.75 12h.007v.008H3.75V12zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0zm-.375 5.25h.007v.008H3.75v-.008zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0z" />
</svg>

                  AI-Generated Summaries</h4>
              <p class="ml-3 mt-1 text-start">
                  Receive concise and coherent summaries of your questions, making it easy to review and reflect on your experiences.
                   </p>

          </div>
          <div class="bg-white font-rope  p-4 rounded-lg">
              <h4 class="ml-3 flex gap-2 justify-start font-bold items-end">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5 mb-0.5 text-orange-500">
<path stroke-linecap="round" stroke-linejoin="round" d="M3.98 8.223A10.477 10.477 0 001.934 12C3.226 16.338 7.244 19.5 12 19.5c.993 0 1.953-.138 2.863-.395M6.228 6.228A10.45 10.45 0 0112 4.5c4.756 0 8.773 3.162 10.065 7.498a10.523 10.523 0 01-4.293 5.774M6.228 6.228L3 3m3.228 3.228l3.65 3.65m7.894 7.894L21 21m-3.228-3.228l-3.65-3.65m0 0a3 3 0 10-4.243-4.243m4.242 4.242L9.88 9.88" />
</svg>


                  Privacy-focused</h4>
              <p class="ml-3 mt-1 text-start">
                  Your data is for your eyes only. We prioritize security and data protection to ensure your information remain confidential.
              </p>

          </div>
          <div class="bg-white font-rope  p-4 rounded-lg">
              <h4 class="ml-3 flex gap-2 justify-start font-bold items-end">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5 mb-0.5 text-purple-500">
<path stroke-linecap="round" stroke-linejoin="round" d="M3.98 8.223A10.477 10.477 0 001.934 12C3.226 16.338 7.244 19.5 12 19.5c.993 0 1.953-.138 2.863-.395M6.228 6.228A10.45 10.45 0 0112 4.5c4.756 0 8.773 3.162 10.065 7.498a10.523 10.523 0 01-4.293 5.774M6.228 6.228L3 3m3.228 3.228l3.65 3.65m7.894 7.894L21 21m-3.228-3.228l-3.65-3.65m0 0a3 3 0 10-4.243-4.243m4.242 4.242L9.88 9.88" />
</svg>


                  Privacy-focused</h4>
              <p class="ml-3 mt-1 text-start">
                  Your data is for your eyes only. We prioritize security and data protection to ensure your information remain confidential.
              </p>

          </div>
          <div class="bg-white font-rope  p-4 rounded-lg">
              <h4 class="ml-3 flex gap-2 justify-start font-bold items-end">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5 mb-0.5 text-orange-500">
<path stroke-linecap="round" stroke-linejoin="round" d="M3.98 8.223A10.477 10.477 0 001.934 12C3.226 16.338 7.244 19.5 12 19.5c.993 0 1.953-.138 2.863-.395M6.228 6.228A10.45 10.45 0 0112 4.5c4.756 0 8.773 3.162 10.065 7.498a10.523 10.523 0 01-4.293 5.774M6.228 6.228L3 3m3.228 3.228l3.65 3.65m7.894 7.894L21 21m-3.228-3.228l-3.65-3.65m0 0a3 3 0 10-4.243-4.243m4.242 4.242L9.88 9.88" />
</svg>


                  Privacy-focused</h4>
              <p class="ml-3 mt-1 text-start">
                  Your data is for your eyes only. We prioritize security and data protection to ensure your information remain confidential.
              </p>

          </div>
          <div class="bg-white font-rope  p-4 rounded-lg">
              <h4 class="ml-3 flex gap-2 justify-start font-bold items-end">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5 mb-0.5 text-green-500">
<path stroke-linecap="round" stroke-linejoin="round" d="M8.25 3v1.5M4.5 8.25H3m18 0h-1.5M4.5 12H3m18 0h-1.5m-15 3.75H3m18 0h-1.5M8.25 19.5V21M12 3v1.5m0 15V21m3.75-18v1.5m0 15V21m-9-1.5h10.5a2.25 2.25 0 002.25-2.25V6.75a2.25 2.25 0 00-2.25-2.25H6.75A2.25 2.25 0 004.5 6.75v10.5a2.25 2.25 0 002.25 2.25zm.75-12h9v9h-9v-9z" />
</svg>



Continuous Improvements</h4>
              <p class="ml-3 mt-1 text-start">
                  Developed by a team that cares, we're continuously working to improve and add new features to NickGPT every single day!
              </p>

          </div>
          
          
      </div>
           
     </div>


     <div class="mt-32 text-[#040406] font-rope">
        <h2 class="font-bold text-start text-4xl">Our Pricing</h2>
        <p class="mt-4 text-start text-[#040406]/80">We offer flexible payment models and pocket friendly <br>  options  for your comfortable and productive work.</p>
        <div class="mt-6 grid grid-cols-3 gap-x-16">
           <div class=" pb-12 rounded-lg bg-white">
              <h2 class=" text-3xl font-bold text-start mt-6 ml-4">Free</h2>
              <p class=" text-start mt-4 ml-4">For individual users</p>
              <hr class="text-gray-300 mt-8 ml-4 mr-4">
              <ul class="mt-8 text-start flex flex-col gap-y-6 ml-4 text-[#040406]">
                 <li class="inline-flex gap-3">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                       <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
                    </svg>
                    Upload one document
                 </li>
                 <li class="inline-flex gap-3">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                       <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
                    </svg>
                    Support for one document type
                 </li>
                 <li class="inline-flex gap-3">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                       <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
                    </svg>
                    5 questions a week
                 </li>
                 <li class="inline-flex gap-3">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                       <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
                    </svg>
                    Share credentials with 3 users
                 </li>
              </ul>
              <h2 class="text-[#040406] text-3xl font-bold text-start mt-8 ml-4">KSH 0 <span class="text-sm">/month</span> </h2>
              <div class="mt-8 ml-4 mr-4 flex justify-center">
                 <button class="bg-[#8b3dff] w-full px-4 py-2 font-rope rounded text-white transition-colors duration-300 cursor-pointer">
                 Buy Now
                 </button>
              </div>
           </div>
           <div class=" pb-12 rounded-lg bg-white">
              <h2 class="text-[#040406] text-3xl font-bold text-start mt-6 ml-4">Premium</h2>
              <p class="text-[#040406] text-start mt-4 ml-4">For a smal team</p>
              <hr class="text-gray-300 mt-8 ml-4 mr-4">
              <ul class="mt-8 text-start flex flex-col gap-y-6 ml-4 text-[#040406]">
                 <li class="inline-flex gap-3">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                       <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
                    </svg>
                    Upload 3 documents
                 </li>
                 <li class="inline-flex gap-3">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                       <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
                    </svg>
                    Support for 3 document types
                 </li>
                 <li class="inline-flex gap-3">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                       <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
                    </svg>
                    30 questions a week
                 </li>
                 <li class="inline-flex gap-3">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                       <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
                    </svg>
                   Access to CRUD models
                 </li>
              </ul>
              <h2 class="text-[#040406] text-3xl font-bold text-start mt-8 ml-4">KSH 4,999 <span class="text-sm">/month</span> </h2>
              <div class="mt-8 ml-4 mr-4 flex justify-center">
                 <button class="bg-[#8b3dff] w-full px-4 py-2 font-rope rounded-lg text-white transition-colors duration-300 cursor-pointer">
                 Buy Now
                 </button>
              </div>
           </div>
           <div class=" pb-12 rounded-lg bg-white">
              <h2 class="[#040406] text-3xl font-bold text-start mt-6 ml-4">Ultimate</h2>
              <p class="[#040406] text-start mt-4 ml-4">For large companies</p>
              <hr class="text-gray-300 mt-8 ml-4 mr-4">
              <ul class="mt-8 text-start flex flex-col gap-y-6 ml-4 [#040406]">
                 <li class="inline-flex gap-3">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                       <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
                    </svg>
                    Upload documents(No limit)
                 </li>
                 <li class="inline-flex gap-3">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                       <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
                    </svg>
                    Support for 20 plus document types
                 </li>
                 <li class="inline-flex gap-3">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                       <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
                    </svg>
                     No limit on questions / week
                 </li>
                 <li class="inline-flex gap-3">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                       <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
                    </svg>
                    Save data, share data, collaborate etc
                 </li>
              </ul>
              <h2 class="text[#040406] text-3xl font-bold text-start mt-8 ml-4">KSH 20,000 <span class="text-sm">/month</span> </h2>
              <div class="mt-8 ml-4 mr-4 font-rope flex justify-center">
                 <button class="bg-[#8b3dff] w-full px-4 py-2 rounded-lg text-white transition-colors duration-300 cursor-pointer">
                 Buy Now
                 </button>
              </div>
           </div>
        </div>
     </div>

     <div class="mt-32 font-rope">
      <div class="border-b pb-16 flex justify-between">
          <div class="text-start ml-3">
              <h3 class="text-[#040406] font-bold text-2xl">Join our newsletter</h3>
              <p class="text-[#040406]/80 text-md">Keep up to date with everything NickGPT</p>
          </div>
          <div class="flex font-rope mt-2 gap-4">
                 <input type="text" class="bg-white p-5 focus:ring-0 focus:outline-none text-[#040406] placeholder:text-[#040406]/80 placeholder:text-xs w-96 py-1.5 rounded-lg" placeholder="Enter your email">
                 <button class="bg-[#8b3dff] px-6 py-2 rounded-lg text-white transition-colors duration-300 cursor-pointer">
                 Subscribe
                 </button>
              </div>

      </div>

      <div class="mt-20  text-[#040406]/80 flex font-rope justify-between">
          <div class="flex gap-5 ml-3">
              <a href="" class="">Privacy Policy</a>
              <a href="" class="">FAQ</a>
              <a href="" class="">Terms and conditions</a>
          </div>
          <div class="flex font-rope mt-2 gap-4">
              <a href="" class="">NickGPT, LLC. 2023 All rights reserved.</a>
          </div>

      </div>
     </div>
  </div>
</div>
</template>

<style>
html {
  background-color:#f3f2f2; 
}
/* 200440 */
/* 272a2f */
/* 0f0f0f */
/* 040406 */
</style>
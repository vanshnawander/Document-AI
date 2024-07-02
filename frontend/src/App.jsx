import { useState } from 'react'
import axios from 'axios'


function App() {
  const [newMessageText,setNewMessageText] = useState('');
  const [messages,setMessages] = useState([]);
  async function sendMessage(ev){
    ev.preventDefault();
    setMessages(prev => ([...prev,{
      text: newMessageText,
      by:"user"}]))
    const {data} = await  axios.post('http://localhost:8000/response',{query:newMessageText})
    setNewMessageText('')
    console.log(data)
    setMessages(prev => ([...prev,data]))
    
    return true;
  }
  return (
   <div className='flex h-screen'>
    <div className="bg-gray-100 w-1/4 flex flex-col">
        <div className="flex-grow">
          <p className='m-5 p-2 text-3xl text-gray-700 text-opacity-100'>
          Welcome to Document AI
          </p>
           <p className='m-5'>
            Ask queries from the data of electoral bonds to get accruate answers
           </p>
      </div>
        </div>
        <div className="bg-white w-3/4 flex flex-col">
        <div className="flex-grow">
        <div className="relative h-full">
              <div className="overflow-y-scroll absolute top-0 left-0 right-0 bottom-2">
                {messages.map(message => (
                  <div className={message.by==='user'? 'text-right':'text:left'}>
                    <div className='text-left inline-block p-2 my-2 mr-4 ml-3 rounded-lg text-lg bg-blue-100 text-gray-500' >
                    {message.text}
                    </div>
                  </div>
                ))}

               </div>
               </div>  
               </div>         
        <form className="flex gap-2 m-2" onSubmit={sendMessage}>
            <input type="text"
                   value={newMessageText}
                   onChange={ev => setNewMessageText(ev.target.value)}
                   placeholder="Type your query here"
                   className="bg-white flex-grow border rounded-lg p-3"/>
            <button type="submit" className="bg-blue-500 p-2 text-white rounded-lg">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6">
                <path strokeLinecap="round" strokeLinejoin="round" d="M6 12L3.269 3.126A59.768 59.768 0 0121.485 12 59.77 59.77 0 013.27 20.876L5.999 12zm0 0h7.5" />
              </svg>
            </button>
          </form>
      
        </div>
   </div>
  )
}

export default App

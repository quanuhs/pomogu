<template>
    <div class="videoconference">
        <div class="video-content">
            <div class="video">
                <label v-show="isOn.video==false" class="username">{{me.name}}</label>
                <video :srcObject="localStream" autoplay muted @click ="goFullscreen('self')" 
                :class="{'fullscreen': ('self' == fullscreenPeer)}">
                </video>
            </div>
            <div v-for="peer in peers" class="video" @click = "goFullscreen(peer)" :class="{'fullscreen': (peer == fullscreenPeer), 'hidden': (peer != fullscreenPeer && fullscreenPeer != null)}">
                <label class="username">MIKE</label>
                <video v-show="peer.show" :srcObject="peer.srcObject" autoplay></video>
            </div>
        </div>

        <div class="control-buttons">
            <button v-if="isAdmin" class="btn btn-secondary" @click.prevent="endCall()">
                <svg xmlns="http://www.w3.org/2000/svg" idth="50%" height="50%" fill="currentColor" viewBox="0 0 512 512"><path d="M288 32c0-17.7-14.3-32-32-32s-32 14.3-32 32V256c0 17.7 14.3 32 32 32s32-14.3 32-32V32zM143.5 120.6c13.6-11.3 15.4-31.5 4.1-45.1s-31.5-15.4-45.1-4.1C49.7 115.4 16 181.8 16 256c0 132.5 107.5 240 240 240s240-107.5 240-240c0-74.2-33.8-140.6-86.6-184.6c-13.6-11.3-33.8-9.4-45.1 4.1s-9.4 33.8 4.1 45.1c38.9 32.3 63.5 81 63.5 135.4c0 97.2-78.8 176-176 176s-176-78.8-176-176c0-54.4 24.7-103.1 63.5-135.4z"/></svg>
            </button>

            <button :class="{'btn-toggled': isOn.video}" class="btn btn-secondary" @click="turnVideo()">
                <svg  v-if="isOn.video" xmlns="http://www.w3.org/2000/svg" width="50%" height="50%" fill="currentColor" viewBox="0 0 576 512">
                    <path d="M0 128C0 92.7 28.7 64 64 64H320c35.3 0 64 28.7 64 64V384c0 35.3-28.7 64-64 64H64c-35.3 0-64-28.7-64-64V128zM559.1 99.8c10.4 5.6 16.9 16.4 16.9 28.2V384c0 11.8-6.5 22.6-16.9 28.2s-23 5-32.9-1.6l-96-64L416 337.1V320 192 174.9l14.2-9.5 96-64c9.8-6.5 22.4-7.2 32.9-1.6z"/></svg>

                <svg v-else xmlns="http://www.w3.org/2000/svg" width="60%" height="60%" fill="currentColor" viewBox="0 0 640 512">
                    <path d="M38.8 5.1C28.4-3.1 13.3-1.2 5.1 9.2S-1.2 34.7 9.2 42.9l592 464c10.4 8.2 25.5 6.3 33.7-4.1s6.3-25.5-4.1-33.7l-86.4-67.7 13.8 9.2c9.8 6.5 22.4 7.2 32.9 1.6s16.9-16.4 16.9-28.2V128c0-11.8-6.5-22.6-16.9-28.2s-23-5-32.9 1.6l-96 64L448 174.9V192 320v5.8l-32-25.1V128c0-35.3-28.7-64-64-64H113.9L38.8 5.1zM407 416.7L32.3 121.5c-.2 2.1-.3 4.3-.3 6.5V384c0 35.3 28.7 64 64 64H352c23.4 0 43.9-12.6 55-31.3z"/></svg>
            </button>

            <button :class="{'btn-toggled': isOn.audio}" class="btn btn-secondary" @click="turnAudio()">
                <svg v-if="isOn.audio" xmlns="http://www.w3.org/2000/svg" width="50%" height="50%" fill="currentColor" class="bi bi-mic-fill" viewBox="0 0 16 16">
                    <path d="M5 3a3 3 0 0 1 6 0v5a3 3 0 0 1-6 0V3z"/>
                    <path d="M3.5 6.5A.5.5 0 0 1 4 7v1a4 4 0 0 0 8 0V7a.5.5 0 0 1 1 0v1a5 5 0 0 1-4.5 4.975V15h3a.5.5 0 0 1 0 1h-7a.5.5 0 0 1 0-1h3v-2.025A5 5 0 0 1 3 8V7a.5.5 0 0 1 .5-.5z"/>
                </svg>

                <svg v-else xmlns="http://www.w3.org/2000/svg" width="50%" height="50%" fill="currentColor" class="bi bi-mic-mute-fill" viewBox="0 0 16 16">
                    <path d="M13 8c0 .564-.094 1.107-.266 1.613l-.814-.814A4.02 4.02 0 0 0 12 8V7a.5.5 0 0 1 1 0v1zm-5 4c.818 0 1.578-.245 2.212-.667l.718.719a4.973 4.973 0 0 1-2.43.923V15h3a.5.5 0 0 1 0 1h-7a.5.5 0 0 1 0-1h3v-2.025A5 5 0 0 1 3 8V7a.5.5 0 0 1 1 0v1a4 4 0 0 0 4 4zm3-9v4.879L5.158 2.037A3.001 3.001 0 0 1 11 3z"/>
                    <path d="M9.486 10.607 5 6.12V8a3 3 0 0 0 4.486 2.607zm-7.84-9.253 12 12 .708-.708-12-12-.708.708z"/>
                </svg>
            </button>

            <button class="btn btn-secondary" @click.prevent="leaveCall()">
                <svg xmlns="http://www.w3.org/2000/svg" width="50%" height="50%" fill="currentColor" viewBox="0 0 512 512">
                    <path d="M377.9 105.9L500.7 228.7c7.2 7.2 11.3 17.1 11.3 27.3s-4.1 20.1-11.3 27.3L377.9 406.1c-6.4 6.4-15 9.9-24 9.9c-18.7 0-33.9-15.2-33.9-33.9l0-62.1-128 0c-17.7 0-32-14.3-32-32l0-64c0-17.7 14.3-32 32-32l128 0 0-62.1c0-18.7 15.2-33.9 33.9-33.9c9 0 17.6 3.6 24 9.9zM160 96L96 96c-17.7 0-32 14.3-32 32l0 256c0 17.7 14.3 32 32 32l64 0c17.7 0 32 14.3 32 32s-14.3 32-32 32l-64 0c-53 0-96-43-96-96L0 128C0 75 43 32 96 32l64 0c17.7 0 32 14.3 32 32s-14.3 32-32 32z"/></svg>

            </button>

        </div>

    </div>
</template>


<script lang="ts">
import {reactive, ref} from 'vue'


let isAdmin: Boolean = ref(false)


async function endCall() {
    let result = confirm("Завершить сессию?")
    if (result){
        // console.log(result)
    }
    
}

</script>

<script setup lang="ts">
import {reactive, ref} from 'vue'
import {useRoute, useRouter} from 'vue-router'
import {getMyProfile} from "../api"


const route = useRoute();
const router = useRouter();
let fullscreenPeer = ref(null);

let me = await getMyProfile()

function goFullscreen(peer: any){
    if (fullscreenPeer.value == peer)
        fullscreenPeer.value = null
    else
        fullscreenPeer.value = peer
}

async function leaveCall() {
    let result = confirm("Покинуть видеочат?")
    if (result){
        ws.close()
        if (isOn.audio){
            turnAudio()
        }
        router.push({path: "/me"})
    }
    
}


let peers:any = reactive({});
const user_id = "" + me.id
const room_id = route.params.id;

let isOn:any = reactive({"video": false, "audio": false});
let localStream:any = ref(new MediaStream());
let  ws: WebSocket;

const response = 
  await fetch("https://turn.pomogu.su/credentials/"+user_id, {
    method: 'GET',
    mode: 'cors',
    headers: {
    'Content-Type': 'application/json'
    },
  });


// const response = await fetch("https://gleegleb.metered.live/api/v1/turn/credentials?apiKey=86fbc86d22b98f2527211402bfb25cad96b6");

const config = await response.json();
// console.log(config)


async function start_media() {
    try{
        // let stream = await navigator.mediaDevices.getUserMedia({'video': false,'audio': false})
        
        // stream.getTracks().forEach(track => {
        //         track.enabled = false
        // });

        // localStream.value = stream

        ws = new WebSocket(`wss://turn.pomogu.su/ws/${room_id}/${user_id}`)

        ws.onopen  = function (event){
            // console.log(event)
            connectToRoom()
        }

        ws.onerror = function (event){
            // console.log(event)
        }

        ws.onmessage = function(event){
            let data = JSON.parse(event.data)
            // console.log(event.data)
            handle_websocket(data)
        }

        ws.onclose = function(event){
            // console.log(event)
        }


    }catch(error){
        alert('Вам нужно разрешить хотя бы аудио');
        console.log(error)
    }

}

await start_media()


async function refreshConnectionPeer(peer_id: any) {
    await create_offer(peer_id)
}


async function turnVideo() {
    
    isOn.video = !isOn.video

    localStream.value.getVideoTracks().forEach((track: { stop: () => void; }) => {
           track.stop() 
           localStream.value.removeTrack(track)
    });

    if (isOn.video){
        try{
            let stream = await navigator.mediaDevices.getUserMedia({video: {width: {exact: 480}, height: {exact: 270}}})
            localStream.value.addTrack(stream.getTracks()[0])
            await changeTrack(localStream.value.getVideoTracks()[0])
        }catch(error){
            isOn.video = false
            return
        }
    }
}

async function turnAudio() {
    
    isOn.audio = !isOn.audio

    localStream.value.getAudioTracks().forEach((track: { stop: () => void; }) => {
        track.stop() 
        localStream.value.removeTrack(track)
    });

    if (isOn.audio){
        try{
            let stream = await navigator.mediaDevices.getUserMedia({"audio": true})
            localStream.value.addTrack(stream.getTracks()[0])
            await changeTrack(localStream.value.getAudioTracks()[0])

        }catch(error){
            isOn.audio = false
            return
        }
    }

}

async function changeTrack(track: MediaStreamTrack){
    for (const [peer_id, value] of Object.entries(peers)){
        let peerConnection: RTCPeerConnection = peers[peer_id].peerConnection
        let sender = peerConnection.getSenders().find(e => e.track?.kind === track.kind);

        if (sender){
            sender.replaceTrack(track)
        }
        else{
            peerConnection.addTrack(track, localStream.value);
            await create_offer(peer_id)
        }
        
    };
}


async function send(peer_id: string, event_name: string, data : any){
    ws.send(JSON.stringify({"from_id": user_id, "to_id": peer_id, "event": event_name, "data": data}))
}


async function connectToRoom() {
    send("-1", "establish_connection", {})
}

async function handle_websocket(data: any) {
    let from_id = data.from_id;

    switch (data.event){
        case "new_connection":
            await new_connection(data.data.peer_id)
            break;
        
        case "establish_connection":
            await establish_connection(data.data.peers)
            break;
        
        case "break_connection":
            await break_connection(data.data.peer_id)
            break;
        
        case "offer":
            await handle_offer(from_id, data.data)
            break;
        
        case "answer":
            await handle_answer(from_id, data.data)
            break;
        
        case "candidate":
            await handle_candidate(from_id, data.data)
            break;

    }

}


async function new_connection(peer_id: string) {
    peers[peer_id] = {"peerConnection": new RTCPeerConnection(config), "srcObject": undefined, "dataChannel": undefined, "peer_id": peer_id, "show": false}
    let peerConnection = peers[peer_id].peerConnection

    // Устанавливаем свой stream для peerConnection
    localStream.value.getTracks().forEach((track: any) => {
        peerConnection.addTrack(track, localStream.value)
    })


    peerConnection.ontrack = (event: { streams: [any]; }) => {
        // Возможно стоит изменить
        const [remoteStream] = event.streams;
        peers[peer_id].srcObject = remoteStream;

        remoteStream.getTracks().forEach((track: any) => {
            track.onunmute = (event) => {

                if (track.kind == "video")
                    peers[peer_id].show = true

            }

            track.onmute = (event) => {
                if (track.kind == "video")
                    peers[peer_id].show = false
            }
        })
    };

    peerConnection.onicecandidate = (event: { candidate: any; }) => {
        if (event.candidate) {
            send(peer_id, "candidate", event.candidate)
        }
    };

    peers[peer_id].dataChannel = peerConnection.createDataChannel("dataChannel")

    const dataChannel = peers[peer_id].dataChannel

    dataChannel.onerror = function (error: any) {
        // console.log("Error occured on datachannel:", error)
    }

    dataChannel.onmessage = function (event: { data: any; }) {
        // console.log("message:", event.data)
    }

    dataChannel.onclose = function () {
        peerConnection.restartIce()
        // console.log("data channel is closed")
        let audio = new Audio('/sounds/sound_left.mp3');
        audio.play();
    }

	 dataChannel.onopen = function (){
        if (isOn.video){
            refreshConnectionPeer(peer_id)
        }
		// console.log("connection opened!")
        let audio = new Audio('/sounds/sound_join.mp3');
        audio.volume = 0.25;
        audio.play();
        
	 }

    peerConnection.ondatachannel = function (event: { channel: any; }) {
        peers[peer_id].dataChannel = event.channel
    }


}


async function establish_connection(peers: any) {
    
    for (const peer_id of peers) {
        if (peer_id == user_id)
            continue;
        
        // console.log(peer_id)
        await new_connection(peer_id)
        await create_offer(peer_id)
    }
    
}

async function create_offer(peer_id: string){
    let peerConnection = peers[peer_id].peerConnection

    // peerConnection.addTransceiver("audio", {
    //     direction: "sendrecv"
    // })

    // peerConnection.addTransceiver("video", {
    //     direction: "sendrecv"
    // })

    // console.log("making offer")
    let offer = await peerConnection.createOffer({offerToReceiveAudio: true})
    await peerConnection.setLocalDescription(offer)
    await send(peer_id, "offer", peerConnection.localDescription)
    return peerConnection.localDescription
}

async function break_connection(peer_id: string) {
    await peers[peer_id].peerConnection.close()
    delete peers[peer_id]
}

async function handle_offer(peer_id: string, offer: RTCSessionDescriptionInit){
    // console.log(peers, peer_id)
    let peerConnection = peers[peer_id].peerConnection
    await peerConnection.setRemoteDescription(new RTCSessionDescription(offer))

    // const p_tca = peerConnection.getTransceivers()[0];
    // const p_tcv = peerConnection.getTransceivers()[1];

    // p_tca.direction = "sendrecv"
    // p_tcv.direction = "sendrecv"


    let answer = await peerConnection.createAnswer()
    await peerConnection.setLocalDescription(answer)
    await send(peer_id, "answer", peerConnection.localDescription)
    return peerConnection.localDescription

}

async function handle_answer(peer_id: string, answer: RTCSessionDescriptionInit) {
    let peerConnection = peers[peer_id].peerConnection
    await peerConnection.setRemoteDescription(new RTCSessionDescription(answer))
}

async function handle_candidate(peer_id: string, candidate: RTCIceCandidateInit | undefined){
    let peerConnection = peers[peer_id].peerConnection
    await peerConnection.addIceCandidate(new RTCIceCandidate(candidate));
}


</script>

<style scoped>

video{
    background-color: black;
    height: 100%;
    width: 100%;

    object-fit: contain;
    object-position: 50% 50%;
    
}

.username{
    color: white; 
    position: absolute; 
    top: 2%;
    background-color: rgba(255, 255, 255, 0.2);
    padding: 5px;
    border-radius: 10px;
}

.video{
    aspect-ratio: 16/9;
    
    background-color: black;
    border: 1px solid black;
    object-fit: contain;
    display: flex;
    justify-content: center;
    min-width: 300px;
    width: 100%;
    height: 100%;
    position: relative;
}

.hidden{
    display: none;
}

.fullscreen{
    position: fixed;
    right: 0;
    bottom: 0;
    min-width: 100%;
    min-height: 100%;
    max-width: 100%;
    max-height: 100%;
}

.video-content{
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: repeat(2, 1fr);
    grid-column-gap: 10px;
    grid-row-gap: 10px;
    align-items: center;
    justify-content: center;
}

.videoconference{
    height: 100vh;
}

.control-buttons > .btn{
    height: 100%;
    aspect-ratio: 1/1;
    background-color: WhiteSmoke;
    color:  rgb(66, 66, 66);

    border-color:  rgb(66, 66, 66);
}

.btn-toggled{
    background-color: rgb(66, 66, 66) !important;
    color: WhiteSmoke !important;
}

.control-buttons{
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    gap: 25px;
    height: 50px;
    width: 100px;

    position: fixed;
    left: 50%;
    bottom: 0;
    margin-bottom: 20px;
    margin-left: -50px;

}



@media all and (max-width: 725px){
    .video-content{
        grid-template-columns: repeat(1, 1fr);
        grid-template-rows: repeat(1, 1fr);
    }
}

</style>
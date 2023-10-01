import { ref, computed, watch} from 'vue';

const api_url = "https://api.pomogu.su/";
const logout_url = api_url + "auth/token/logout";
const login_url = api_url + "auth/token/login";
const register_url = api_url + "auth/register";


export let authorised = ref(false)


await getMyProfile()



export async function createAccount(email, password) {
    const res = await fetch(api_url+"users/me", {method: "get", credentials: "include"})
    const finalRes = await res.json();
    console.log(finalRes);
}

export async function login(username, password) {
    const request = new Request(login_url, {
        method: "POST",
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        credentials: "include",

        body: new URLSearchParams({
            'username': username,
            'password': password,
            'grant_type': 'password'
        })
    })

    const result = await fetch(request)

    if (result.ok){
        authorised = true;
    }
    
    await pass_for_errors(result)
    
    getMyProfile()
    return result

}

export async function logout(){
    const request = new Request(logout_url, {
        method: "POST",
        credentials: "include",})

    const result = await fetch(request)
    await pass_for_errors(result)

    if (result.ok){
        authorised = false;
    }
    
    return result
}

export async function register(email, password, name, birthday){
    const request = new Request(register_url, {
        method: "POST",
        headers: { 
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },

        body: JSON.stringify({
            'email': email,
            'password': password,
            'birthday': birthday,
            'name': name
        })
    })


    const result = await fetch(request)
    await pass_for_errors(result)

    if (result.ok){
        await login(email, password)
    }
    
    return result
}

export async function getMyProfile(){
    const result = await fetch(api_url+"users/me", {method: "get", credentials: "include"})

    const result_data = await result.json();

    if (result.ok){
        authorised = true
    }

    await pass_for_errors(result)
    return result_data
}

export async function getTherapistProfile(){
    const result = await fetch(api_url+"therapist/me", {method: "get", credentials: "include"})

    const result_data = await result.json();
    if (result.status == 404)
        return {"error": true}

    await pass_for_errors(result)
    return result_data
}


export async function getMySessions(showHistory){

    const result = await fetch(`${api_url}sessions/client/all?history=${showHistory}`, {method: "get", credentials: "include"})
    const result_data = await result.json();

    await pass_for_errors(result)
    return result_data
}


export async function getMethonds(){
    const result = await fetch(api_url+"methods/", {
        method: "GET"
    })
    
    const result_data = await result.json();
    await pass_for_errors(result)

    return result_data
}

export async function getSpeciality(){
    const result = await fetch(api_url+"tags/", {
        method: "GET"
    })
    
    const result_data = await result.json();
    await pass_for_errors(result)

    return result_data
}

export async function getTherapists(){
    const result = await fetch(api_url+"therapist/all", {
        method: "GET"
    })
    
    const result_data = await result.json();
    await pass_for_errors(result)

    return result_data
}

async function pass_for_errors(result){
    switch (result.status){
        case 401:
            authorised = false;
            break;
    }
}
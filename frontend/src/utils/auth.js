import axios from "axios";

export function logout(cookie) {
    cookie.delete('id')
    cookie.delete('email')
    cookie.delete('access')
    cookie.delete('access_exp')
    cookie.delete('refresh')
    cookie.delete('refresh_exp')
}

export function updateRefresh(cookie, email, refresh_token) {
    return axios.post(process.env.VUE_APP_SERVER_HOST + 'auth/token/', {
        'email': email,
        'token': refresh_token
    }).then(
        response => {
            cookie.set('id', response.data.email)
            cookie.set('email', response.data.email)
            cookie.set('access', response.data.access.token)
            cookie.set('access_exp', response.data.access.exp)
            cookie.set('refresh', response.data.refresh.token)
            cookie.set('refresh_exp', response.data.refresh.exp)
        }
    )
}
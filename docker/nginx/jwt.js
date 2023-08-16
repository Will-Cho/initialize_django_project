function decode_jwt(data) {
    var parts = data.split('.').slice(0, 2)
        .map(v => Buffer.from(v, 'base64url').toString())
        .map(JSON.parse);
    return { headers: parts[0], payload: parts[1] };
}

function get_user_email(r) {
    try {
        return decode_jwt(r.headersIn.Authorization.slice(7)).payload.email;
    } catch (e) {
        return undefined;
    }
}

export default { get_user_email }

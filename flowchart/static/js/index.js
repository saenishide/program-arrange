createFlowchart = function () {
    fetch('/flowchart/create', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken') // CSRFトークンを含める
        }
    })
        .then(response => response.json())
        ;
}

function getCookie(data) {
    const cookieData = document.cookie;
    const csrfToken = cookieData.split(';').find(cookie => cookie.trim().startsWith(data));
    if (!csrfToken) {
        return null;
    }
    return csrfToken.split('=')[1];
}
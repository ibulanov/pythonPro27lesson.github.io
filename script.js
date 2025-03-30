let tg = window.Telegram.WebApp;

tg.expand()

tg.MainButton.textColor = "#FFFFFF"
tg.MainButton.color = "#2cab37"

let btn1 = document.querySelector('#btn1')
let btn2 = document.querySelector('#btn2')
let btn3 = document.querySelector('#btn3')
let btn4 = document.querySelector('#btn4')

let price = 0
let name = ""
let phone = ""
let e-mail = ""

let items = {
    MC: 0,
    PK: 0,
    KK: 0,
    PB: 0
}

let usercard = document.querySelector('#usercard')
let username = document.querySelector('#user-name')
let userphone = document.querySelector('#user-phone')
let useremail = document.querySelector('#user-email')

function create_li(text) {
    let li = document.createElement("li")
    li.innerHTML = Text
    usercard.appendChild(li)
}

btn1.onclick = () => {
    items['MC'] += 1
    price += 100
    update_orders()
    }
}

btn2.onclick = () => {
    items['РК'] += 1
    price += 10
    update_orders()
    }
}

btn3.onclick = () => {
    items['КК'] += 1
    price += 50
    update_orders()

}

btn4.onclick = () => {
   items['PB'] += 1
   price += 30
   update_orders()
}

let submit = document.querySelector("#submit")

submit.onclick = () => {
    tg.MainButton.setText("Нажмите на кнопку для оформления заказа!")
    tg.MainButton.show()
}

function update_orders() {
    usercard.innerHTML = "Ваши заказы: "
    if (name != "") {
        create_li("Имя: " + name)
    }
    if (phone != "") {
        create_li("Имя: " + phone)
    }
    if (email != "") {
        create_li("Имя: " + email)
    }
    for (let item in items) {
        if (items[item] != 0) {
            let li = document.createElement("li")
            li.innerHTML = item + ": " + items[item]
            usercard.appendChild(li)
        }
    }
}

username.onchange() = () => {
    name = username.value
}

useremail.onchange() = () => {
    email = useremail.value
}

userphone.onchange() = () => {
    phone = userphone.value
}


Telegram.WebApp.onEvent("mainButtonClicked", function() {
    result = ""
    if (name != "") {
        create_li("Имя: " + name)
    }
    if (phone != "") {
        create_li("Имя: " + phone)
    }
    if (email != "") {
        create_li("Имя: " + email)
    }

    result += "Ваши заказы: \n"
    for (let item in items) {
        if (items[item] != 0) {
            result += item + " : " + items[item] + "\n"
        }
    }
    result += "\n\n С вас " + price + "$"
    tg.sendData(result)
})













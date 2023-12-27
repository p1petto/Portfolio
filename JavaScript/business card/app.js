'use strict';

function drawCard(){
    let card = document.getElementById('card');

    while (card.firstChild) {
        card.removeChild(card.lastChild);
    }
    
    let form = document.forms.form;

    let institution = form.elements.institution
    let fullName = form.elements.fullName
    let post = form.elements.post
    let phone = form.elements.phone
    let mail = form.elements.mail
    let address = form.elements.address

    let institutionCard =  document.createElement('div');
    institutionCard.setAttribute('class', 'card__institution');
    institutionCard.textContent = institution.value;
    card.appendChild(institutionCard);

    let mainCard =  document.createElement('div');
    mainCard.setAttribute('class', 'card__main');
    card.appendChild(mainCard);

    let fullNameCard =  document.createElement('div');
    fullNameCard.setAttribute('class', 'card__name');
    fullNameCard.textContent = fullName.value;
    fullNameCard.style.fontSize = form.elements.fullNameRadio.value
    fullNameCard.style.textAlign = form.elements.fullNameAlign.value
    fullNameCard.style.color = form.elements.nameColor.value
    mainCard.appendChild(fullNameCard);

    let postCard =  document.createElement('div');
    postCard.setAttribute('class', 'card__post');
    postCard.textContent = post.value;
    postCard.style.fontSize = form.elements.postRadio.value
    postCard.style.textAlign = form.elements.postAlign.value
    postCard.style.color = form.elements.postColor.value
    mainCard.appendChild(postCard);

    let supportiveContainerCard =  document.createElement('div');
    supportiveContainerCard.setAttribute('class', 'card__supportive');
    card.appendChild(supportiveContainerCard);

    let contactCard =  document.createElement('div');
    contactCard.setAttribute('class', 'card__cotact');
    supportiveContainerCard.appendChild(contactCard);

    let phoneCard =  document.createElement('div');
    phoneCard.setAttribute('class', 'card__phone');
    phoneCard.textContent = phone.value;
    contactCard.appendChild(phoneCard);

    let mailCard =  document.createElement('div');
    mailCard.setAttribute('class', 'card__mail');
    mailCard.textContent = mail.value;
    contactCard.appendChild(mailCard);

    let addressCard =  document.createElement('div');
    addressCard.setAttribute('class', 'card__address');
    addressCard.textContent = address.value;
    contactCard.appendChild(addressCard);
}



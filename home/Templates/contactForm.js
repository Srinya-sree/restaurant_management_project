const form = document.createElement('form');
form.id = 'contactForm';
const heading = document.createElement('h2');
heading.textContent='Contact Us';
document.body.appendChild(heading);

//Name label and input
const nameLabel = document.childElement('label');
nameLabel.setAttribute('for', 'name');
nameLabel.textContent='Name';
const nameInput = document.createElement('input');
nameInput.type='text';
nameInput.id='name';
nameInput.name='name';
document.body.appendChild(nameLabel);
document.body.appendChild(nameInput);
document.body.appendChild(document.createElement('br'));
document.body.appendChild(document.createElement('br'));
//Email label and inputs
const emailLabel = document.createElement('label');
emailLabel.setAttribute('for','email');
emailLabel.textContent='Email';
const emailInput = document.createElement('label');
emailInput.type='email';
emailInput.id='email';
emailInput.name='email';
document.body.appendChild(emailLabel);
document.body.appendChild(emailInput);
document.body.appendChild(document.createElement('br'));
document.body.appendChild(document.createElement('br'));

//submit button
const submitButton = document.createElement('button');
submitButton.type = 'submit';
submitButton.textContent='Submit';
document.body.appendChild(submitButton);

//Error Meassage
const errorMessage = document.createElement('p');
errorMessage.id = 'errorMessage';
errorMessage.style.color = 'red';
document.body.appendChild(errorMessage);

//Append form to body
document.body.appendChild(form);

//Add client-side validation

form.addEventListener('submit',function(event){
    const name = nameInput.value.trim();
    const email = emailInput.value.trim();
    if(name === '' || email === ''){
        event.preventDefault();
        errorMessage.textContent = 'Please fill in the both Name and Email fields.';
    }else{
        errorMessage.textContent='';
        alert('Form submittedsuccessfully!');
    }
});
const generateBtn = document.getElementById("generate");
const passwordEls = document.querySelectorAll(".password");
const popUp = document.getElementById("pop-up");
const imgInput = document.getElementById("image-input");

/*------------------------------------*\
  #EVENT-HANDLERS
\*------------------------------------*/

function updateLength(event) {
	const number = Math.floor(event.target.value);

	if (number >= 8 && number <= 20) {
		passwordLength = number;
	} else {
		alert("Password length must be between 8 and 20 characters.");
	}

	event.target.value = passwordLength;
}

function inputStepper(event) {
	if (event.target.id === "decrement") {
		lengthInput.stepDown();
	}

	if (event.target.id === "increment") {
		lengthInput.stepUp();
	}

	passwordLength = lengthInput.value;
}

async function copyToClipboard(event) {
	const password = event.target.textContent;
	try {
		await navigator.clipboard.writeText(password);
	} catch (err) {
		console.log("Clipboard access denied. Time to go old school...");
		copyUsingExecCommand(password);
	}

	// show a pop-up to notify the user
	clearTimeout(timeoutId);
	popUp.style.opacity = 0.9;
	timeoutId = setTimeout(() => (popUp.style.opacity = 0), 1000);
}

function copyUsingExecCommand(text) {
	const input = document.createElement("input");
	input.value = text;
	input.readOnly = true;
	input.style = {
		position: "absolute",
		left: "-9999px",
	};
	document.body.append(input);
	input.select();
	document.execCommand("copy");
	input.remove();
}

/*------------------------------------*\
  #GENERATOR-FUNCTIONS
\*------------------------------------*/

function generatePasswords() {
	// generate a list of passwords based on the number of password elements
	let passwords = [];
	for (let i = 0; i < passwordEls.length; i++) {
		const password = generatePassword();
		passwords.push(password);
	}

	// display the passwords on the page
	for (let i = 0; i < passwords.length; i++) {
		passwordEls[i].textContent = passwords[i];
		passwordEls[i].classList.remove("hidden");
	}
}

// Initialize
let timeoutId;
let passwordLength = 15;
lengthInput.value = passwordLength;

generateBtn.addEventListener("click", generatePasswords);

passwordEls.forEach((element) => {
	element.addEventListener("click", copyToClipboard);
});

imgInput.addEventListener("change", function () {
	const reader = new FileReader();
	reader.addEventListener("load", () => {
		const uploaded_image = reader.result;
		document.querySelector(
			"#display-image"
		).style.backgroundImage = `url(${uploaded_image})`;
	});
	reader.readAsDataURL(this.files[0]);
});
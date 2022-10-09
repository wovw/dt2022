const passwordEls = document.querySelectorAll(".password");
const popUp = document.getElementById("pop-up");
const imgLabel = document.querySelector(".custom-upload");

/*------------------------------------*\
  #EVENT-HANDLERS
\*------------------------------------*/

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

function loadImg() {
	const selectedFile = document.getElementById("img-upload").files[0];
	console.log("1");
	const reader = new FileReader();
	reader.addEventListener("load", () => {
		const uploaded_image = reader.result;
		const displayImg = document.querySelector("#display-image");
		displayImg.classList.remove("hidden");
		displayImg.style.backgroundImage = `url(${uploaded_image})`;
	});
	reader.readAsDataURL(selectedFile);

	loadSentences(selectedFile);
}

function loadSentences(img) {
	// upload image
	let formData = new FormData();
	formData.append("file", img);
	const requestOptions = {
		headers: {
			"Content-Type": img.contentType,
		},
		mode: "no-cors",
		method: "POST",
		files: img,
		body: formData,
	};
	fetch("http://127.0.0.1:5000/upload", requestOptions).then(() => {
		console.log("1");
	});

	// run python

	// load sentences
	const sentencesFile = 1;
}

// Initialize
let timeoutId;

// event listeners
passwordEls.forEach((element) => {
	element.addEventListener("click", copyToClipboard);
});

imgLabel.addEventListener("change", loadImg);

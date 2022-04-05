const getUrlParameter = (key) => {
	const urlParams = new URLSearchParams(window.location.search);
	return urlParams.get(key);
}

document.addEventListener("DOMContentLoaded", function (event) {
	const submitQuestBtn = document.getElementById('submit-quest-btn');
	const questPasswordInput = document.getElementById('quest-password-input');

	submitQuestBtn.addEventListener('click', function (event) {
		event.preventDefault();

		const questPassword = questPasswordInput.value;

		if (!questPassword) {
			// Alert swal
			Swal.fire({
				title: 'Error',
				text: 'Please enter a password',
				icon: 'error',
				button: 'Ok'
			});
		}
		// Clear input
		questPasswordInput.value = '';

		// get type in url parram
		const type = getUrlParameter('type');
		console.log(type)

	});
});

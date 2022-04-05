const getUser = async () => {
	// Call /auth/user GET api and return user data
	return fetch('/auth/user', {
		method: 'GET'
	}).then(async (res) => {
		const data = await res.json();
		return data;
	});
}

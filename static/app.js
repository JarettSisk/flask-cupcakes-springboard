// Elements
let cupcakeList = document.querySelector('.cupcake-list');
let addCupcakeForm = document.querySelector('.add-cupcake-form')


async function appendCupcakes() {
    cupcakeList.innerHTML = "";
    try {
        const response = await axios.get('/api/cupcakes');
        cupcakes = response.data.cupcakes;
        for(cupcake of cupcakes) {
            let listEl = document.createElement('LI');
            let imageEl = document.createElement("IMG");
            imageEl.classList.add("cupcake-image");
            imageEl.setAttribute('src', cupcake.image);
            let pEl = document.createElement("P");
            pEl.innerText = `ID: ${cupcake.id} Flavor: ${cupcake.flavor} Rating: ${cupcake.rating} Size: ${cupcake.size}`;

            listEl.append(imageEl);
            listEl.append(pEl);
            cupcakeList.append(listEl);
        }
    } catch (error) {
        console.error(error);
    }
}
// initial call
appendCupcakes()

// Add new cupcake
addCupcakeForm.addEventListener('submit', async function(e) {
    e.preventDefault();
    console.log(e.target.flavor.value)
    let image = null;
    if (e.target.image.value != "") {
        image = e.target.image.value;
    }
    
    await axios.post('/api/cupcakes', {
        flavor: e.target.flavor.value,
        size: e.target.size.value,
        rating: e.target.rating.value,
        image: image
        })
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
    appendCupcakes();
    this.reset();
})
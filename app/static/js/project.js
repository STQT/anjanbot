function redirectToMain() {
    window.location.href = "/telegram/";
}

function deleteProduct(productId) {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    const index = cart.indexOf(productId);
    console.log(cart, "cart");
    console.log(index)
    if (index > -1) {
        cart.splice(index, 1);
        localStorage.setItem('cart', JSON.stringify(cart));
        document.getElementById(`product-${productId}`).remove();
        console.log(`Removed product with ID ${productId} from the cart`);
    } else {
        redirectToMain();
    }
}

function increaseCount(productId) {
    const countElement = document.getElementById(`prod-${productId}`);
    if (countElement) {
        let count = parseInt(countElement.innerText);
        count++;
        countElement.innerText = count;
    } else {
        redirectToMain();
    }
}

function decreaseCount(productId) {
    const countElement = document.getElementById(`prod-${productId}`);
    if (countElement) {
        let count = parseInt(countElement.innerText);
        if (count > 1) {
            count--;
            countElement.innerText = count;
        } else {
            console.log(`Minimum count reached for product with ID ${productId}`);
        }
    } else {
        redirectToMain();
    }
}



function addOffer()
{ 
    const newOfferInput = document.getElementById("newOfferInput");
    const userOfferInput = document.getElementById("newOfferInput");
    
    
    const newOfferText = newOfferInput.value.trim(); 
    
    if (newOfferText !== "")
    {
            const listItem = document.createElement("li");
            listItem.textContent = newOfferText;
            userOffersList.appendChild(listItem);
            newOfferInput.value = ""; // Clear the input field
    }
    

}

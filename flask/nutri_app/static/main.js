

function Calo()
{
    var h=document.getElementById('hi').value;
    var w=document.getElementById('we').value;
    var g=document.getElementById('g').value;
    var age=document.getElementById('age').value;

    var calo= (10* w/1+ 6.25 * h/1 - 5 * age/1 + 5);
    var calom = calo * 1.4;

    document.getElementById("resultcal").innerHTML="Your Daily Calories Intake:  " +calom;

    const proteins =calom*0.12;
    const carbs =calom*0.60;
    const fats =calom*0.27;

    let data2= [proteins, fats, carbs];
    const ctx = document.getElementById('myChart').getContext('2d');
    let myChart = new Chart(ctx,{
        type:'doughnut' ,
        data:{
            labels: ['Proteins','Fats','Carbs'],
            datasets : [
                {
                    label : '# of votes',
                    data : data2,
                    backgroundColor :['#2adece','#dd3b79', '#ff766b'],
                    borderwidth:0.1
                }
            ]
        }

});

}

function Clear()
{
    document.getElementById('resultcal').innerHTML="";
}

const search = document.getElementById('search');
const submit = document.getElementById('submit');
const random = document.getElementById('random');
const mealEl = document.getElementById('meals');
const resultHeading = document.getElementsByClassName('result-heading');
const single_mealEl = document.getElementById('single-meal');
 
// search for meals
function searchMeal(e){
    e.preventDefault();

// clear sigle meal
single_mealEl.innerHTML="";

//get search meal
const term = search.value;
 
//check for empty
if(term.trim()){
    fetch(`https://www.themealdb.com/api/json/v1/1/search.php?s=${term}`)

.then((res) => res.json())
 .then((data) =>{
    console.log(data);
    resultHeading.innerHTML = `<h2>Search Result For ${term}`;
    if(data.meals === null ){
        resultHeading.innerHTML = `<h2>There Are No Result For ${term}`;
    }else{
        mealEl.innerHTML = data.meals.map(
            meal => `
            <div class="meal">
            <img src="${meal.strMealThumb}" alt="${meal.strMeal}">
            <div class="meal-info" data-mealId="${meal.idMeal}">
            <h3>${meal.strMeal}</h3>
            </div>
            </div>`

        
        ).join("");
     }

      });

    }else{
        alert("please insert a value in Search");
    }
}


// fetch meal byc id
function getMealById(mealId){
    fetch(`https://www.themealdb.com/api/json/v1/1/lookup.php?i=${mealId}`)
    .then((res)  => res.json())
    .then((data) => {
        console.log(data);
      const meal = data.meals[0];
      addMealToDom(meal);
    });
}
//random meal
function randomMeal(){
    mealEl.innerHTML="";
    resultHeading.innerHTML="";

    fetch(`https://www.themealdb.com/api/json/v1/1/random.php`)
    .then(res => res.json()).then(data =>{
       const meal = data.meals[0];
       addMealToDom(meal);
})

}
//add meal to dom
function addMealToDom(meal){
    const ingredients = [];
     for(let i=1; i<=20; i++){
        if(meal[`strIngredient${i}`]) {
            ingredients.push(`${meal[`strIngredient${i}`]}- ${
                meal[`strMeasure${i}`]}
            `);
        }else{
            break;
        }
    
        
    }
    single_mealEl.innerHTML = `
    <div class="single-meal">
    <h1>${meal.strMeal}</h1>
    <img src="${meal.strMealThumb}" alt="${meal.strMeal}"/>
    <div class="single-meal-info">
    ${meal.strCategory ? `<p>${meal.strCategory}</p>`: ''}
    ${meal.strArea ? `<p>${meal.strArea}</p>`:''}
    </div>
    <div class="main">
    <p>${meal.strInstructions}</p>
    <h2>Ingredients</h2>
    <ul>${ingredients.map(ing => `<li>${ing}</li>`).join('')}
    </ul>
    </div>
    </div>
    `;
}
// event listners
submit.addEventListener("submit",searchMeal);
random.addEventListener("click",randomMeal);
mealEl.addEventListener("click",e => {
    const mealInfo = e.path.find(item => {
        if(item.classList){
            return item.classList.contains("meal-info");
        }else{
            return false;
        }
    });
 if(mealInfo){
    const mealId = mealInfo.getAttribute("data-mealid");
    getMealById(mealId);
 }
})
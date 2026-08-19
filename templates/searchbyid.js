let table = document.getElementById('table');
const EmployeeId = document.getElementById('Employee_id');
const Search = document.getElementById('Id_search');
Search.addEventListener('click',async ()=>{
    const serverResponse = await fetch('/admin/dashboard/searchbyid',{
        method:'POST',
        headers:{'Content-Type':'application/json'},
        body:JSON.stringify({
            'Employee_id':EmployeeId.value
        })
        }
    );

    data = await serverResponse.json();
    console.log(data)
    if(data.sucess){
        table.innerHTML = `
        <h1 class='detail'>Employee Name : ${data.data.Employee_Name}</h1>
        <h2 class='detail'>Desigination : ${data.data.Desigination}</h2>
        <h2 class='detail'>Department ID : ${data.data.Department_Id}</h2>
        <h2 class='detail>Employee Email : ${data.data.Email_Id}</h2>
        <h2 class='detail'>Employee Mobile Number : ${data.data.Mobile_Number}</h2>
        <h2 class='detail>Employee added by User : ${data.data.Added_By}</h2>
        <h2 class='detail'>Employee Joined on  : ${data.data.Added_at}</h2>
        `;
    }


});
//first button 
const searchbyid = document.getElementById('searchbyid');
searchbyid.addEventListener('click',()=>{
    const DOM = document.getElementsByName('display');
    console.log(DOM);
    for(let element of DOM){
        element.style.display='none';
    }
    const display = document.getElementById('searchbyid_display');
    display.style.display = '';

});
//first  button end

// second button 

const presenttoday = document.getElementById('presenttoday');
presenttoday.addEventListener('click',async ()=>{

    const DOM = document.getElementsByName('display');
    console.log(DOM);
    for(let element of DOM){
        element.style.display='none';
    }
    const display = document.getElementById('presenttoday_display');
    display.style.display = '';
    const dateFromUser = document.getElementById('checkDate')
    const presenttoday_table = document.getElementById('present_today_table');
    const searchdate = document.getElementById('searchbydate');
    searchdate.addEventListener('click',async ()=>{
        const serverResponse = await fetch('/admin/dashboard/presenttoday',{
        method:'POST',
        headers:{
            'Content-Type':'Application/json'
        },
        body:JSON.stringify({
            'date':dateFromUser.value
        })
        
    });
    const response = await serverResponse.json();
    console.log(response);

    if (response.sucess) {

        presenttoday_table.innerHTML = '';

        for (let employee of response.data) {

            presenttoday_table.innerHTML += `
                <tr>
                    <td>${employee.Name}</td>
                    <td>${employee.Mobile}</td>
                    <td>${employee.Email_Id}</td>
                    <td>${employee.Department_Id}</td>
                    <td>${employee.Department_Name ?? 'N/A'}</td>
                    <td>${employee.Check_In}</td>
                    <td>${employee.Attendence_Date}</td>
                </tr>
            `;
            }
        }

    })



});

//second button end
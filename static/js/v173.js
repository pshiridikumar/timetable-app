function myfunction(){
    var mq = window.matchMedia( "(min-width: 768px)" );
    mq.addListener(WidthChange);
    WidthChange(mq);
    }
function WidthChange(mq){
    console.log(mq)
    var bool=mq.matches
    if(!(bool)){
        console.log("not ok");
        alert("you are opening in mobile;")
        location.reload();

    }
   
}
	/*if (bool) {
		var flag=1

        console.log("ok ");
		// window width is at least 500px
	  } else {
          console.log("not ok");
		  alert("you are opening in mobile;")
		// window width is less than 500px
	  }*/



function edit_row(no){
	document.getElementById("edit"+no).style.display="none";
	var l =document.getElementsByClassName("row_no"+no);
	var i;
	for(i=0;i<l.length;i++){
		var k=l[i];
		var y
		y=`row_no${no}`;
		k.innerHTML="<input type='text' class='edit_data"+no+"' value='"+l[i].innerText+"' style='width:140px'>";
	}
  
	
}
function save_row(no){
	document.getElementById("edit"+no).style="height:25px;font-size:10px;padding:5px;padding-top:2px;padding-bottom:2px";
	var l=document.getElementsByClassName("edit_data"+no);
	var t=document.getElementsByClassName("row_no"+no);
	var i;
	var arr=new Array();
	console.log(l.length);
	console.log(t.length);
	for(i=0;i<t.length;i++){
		arr[i]=l[i].value;
	}
	for(i=0;i<t.length;i++){
		var k=t[i];
		k.innerHTML=arr[i];
	}
}
function tryaj(){
	var c=document.getElementById("clicked").value="....processing";
	var l =document.getElementsByTagName("tr");
    console.log(l.length);
    var arr= new Array();
    var tableheads=document.getElementsByTagName("th");
    var k =new Array();
    for(i=0;i<tableheads.length-1;i++){
    	k.push(tableheads[i].innerText);
    }
    console.log(k)
    arr.push(k);
    for(i=0;i<l.length;i++){
    	var arr1= new Array();
    	var row=document.getElementsByClassName("row_no"+i);
    	for(j=0;j<row.length;j++){
    		arr1.push(row[j].innerText);
    		console.log(arr1);
    	}
    	arr.push(arr1);
    }
    console.log(k)
    console.log(arr);
    var z= document.getElementsByClassName("nextf");
	$.post("/pie",{"array":`${arr}`,"rowlen":`${tableheads.length}`,"arrlen":`${arr.length}`},function(data,status)
            {
            	 var z= document.getElementsByClassName("nextf");
				    if(z.length==0){
					    var br = document.createElement("br");  
					    var form=document.createElement("form");
					    form.setAttribute("action","/finalsub");
					    form.setAttribute("class","nextf");
					    var s = document.createElement("input"); 
					    s.setAttribute("type", "submit"); 
					    s.setAttribute("value", "Click here to continue.."); 
					    s.setAttribute("class", "btn btn-dark"); 
					    s.setAttribute("id", "subbut");
					    form.appendChild(s);
                        form.style="position:relative;left:350px;display:inline"

					    var c=document.getElementsByClassName("heading")
					    c[0].appendChild(form);

					}
					var rem=document.querySelectorAll('#clicked');
					$(rem[rem.length - 1]).remove(); 

					var sub= document.getElementById("subbut");
					sub.style="position:relative;left:300px;width:200px;height:40px;font-size:15px";
          }
     );          
}
function fix_slots(){
	var t=document.getElementById("studfix");
	var b=document.getElementsByClassName("block3");
    var assib=document.querySelectorAll("#assib");
    $(assib[assib.length-1]).remove();
    console.log("hello world");
    /*
	if(t==null){
        console.log("first one ok");
		var x=document.createElement("input");
		x.setAttribute("type","button");
		x.setAttribute("value","Students");
		x.setAttribute("class","btn btn-dark");
		x.setAttribute("id","studfix");
        x.style="width:170px;height:40px;position:relative;left:560px;top:60px"
		b[b.length-1].appendChild(x);
	}
	var t1=document.getElementById("facultyfix");
	if(t1==null){
        console.log("seond one ok");
		var y=document.createElement("input");
		y.setAttribute("type","button");
		y.setAttribute("class","btn btn-dark");
		y.setAttribute("value","faculty");
		y.setAttribute("id","facultyfix");
		y.setAttribute("href","#");
        y.style="width:170px;height:40px;position:relative;left:580px;top:60px"
		b[b.length-1].appendChild(y);
	}
		var t1=document.getElementById("facultyfix");
        console.log(t1);
		t1.onclick=function(){*/
			$.post("/fac_choices",{},function(data,status){
				console.log(data.keys);
				var ge=document.getElementById("fac_button");
				if(ge==null){
					var br = document.createElement("br");
					var dbut=document.createElement("div")
					dbut.setAttribute("class","dropdown");
					var bu=document.createElement("button")
					bu.setAttribute("class","dropbtn");
					bu.setAttribute("id","fac_button");
					bu.innerText="Select faculty";
					dbut.appendChild(bu);
					var ind=document.createElement("div");
					ind.setAttribute("class","dropdown-content");
					for(i=0;i<data.keys.length;i++){
						var anchor=document.createElement("a");
						anchor.setAttribute("href","#")
						anchor.setAttribute("id",`fac${i}`);
						anchor.setAttribute("onclick",`javascript:fac_clicked(${i})`);
						anchor.innerText=data.keys[i];
						ind.appendChild(anchor);
					}
					dbut.appendChild(ind);
					/*dbut.onclick=function(){
						var dis=ind.style.display;
                        if(dis!="block"){
                            ind.style="display:block";
                        }
                        else{
                            ind.style="display:none";
                        }
                    }*/

					
                    dbut.style="background-color:black;color:white;position:relative;left:620px;top:20px";
					b[b.length-1].appendChild(dbut);
				}
			})
		

		//t=document.getElementById("studfix");
		//t.onclick=function(){
			$.post("/stud_choices",{},function(data,status){
				console.log(data.keys1);
				var sg =document.getElementById("sel_stud");
				console.log(sg);
				if(sg==null){
					console.log(sg);
					var br = document.createElement("br");
					var dbut=document.createElement("div");
					dbut.setAttribute("class","dropdown");
					var bu=document.createElement("button");
					bu.setAttribute("class","dropbtn");
					bu.setAttribute("id","sel_stud");
					bu.innerText="Select Students";
					dbut.appendChild(bu);
					var ind=document.createElement("div");
					ind.setAttribute("class","dropdown-content");
					for(i=0;i<data.keys1.length;i++){
						var anchor=document.createElement("a");
						anchor.setAttribute("href","#");
						anchor.setAttribute("onclick",`javascript:stud_clicked(${i})`);
						anchor.setAttribute("id",`stud${i}`);
						anchor.innerText=data.keys1[i];
						ind.appendChild(anchor);
					}
					dbut.appendChild(ind);
                    console.log(ind.style);
					/*dbut.onclick=function(){
						var dis=ind.style.display;
                        if(dis!="block"){
                            ind.style="display:block";
                        }
                        else{
                            ind.style="display:none";
                        }
                    }*/

                    dbut.style="background-color:black;color:white;position:relative;left:640px;top:20px"
					b[b.length-1].appendChild(dbut);
				}
			})
			

		
	
}

function fac_clicked(n){
	var c=document.getElementById("fac"+n);
	$.post("/fac_sel",{"selected":c.innerText},function(data,status){
		console.log(data.dic);
		var ar=data.dic;
		var facl=data.dic[0];
		var alloted= new Array();
		for(i=0;i<facl.length;i++){
			alloted.push(facl[i][1]);
		}
		var b=document.getElementsByClassName("block3");
		var alr=document.getElementsByClassName("allotment");
		var nlr=document.getElementsByTagName("h5");
		console.log(nlr,alr)
		if(alr.length!=0){
			$(alr[alr.length-1]).remove();
			console.log(nlr);
			if(nlr.length!=0){
				$(nlr[nlr.length-1].remove());
				console.log(alr.length);
			}
		}
		var name=document.createElement("h5");
		name.setAttribute("class","namefac");
		name.innerText=c.innerText;
        name.style="color:black;text-shadow: 0 0 20px white, 0 0 30px white, 0 0 40px white, 0 0 50px white, 0 0 60px white, 0 0 70px white, 0 0 80px white;position:relative;top:30px;text-align:center;font-size:30px"
		b[b.length-1].appendChild(name);
		var colum=["",1,2,3,4,5,6,7];
		var block=document.createElement("div")
		block.setAttribute("class","allotment");
		var tab=document.createElement("table");
		tab.setAttribute("class","table table-dark table-hover");
        tab.style="height:400px";
		the=document.createElement("thead");
		var tr=document.createElement("tr");
		var j;
		var k;
		for(j=0;j<colum.length;j++){
			var th=document.createElement("th");
			th.setAttribute("scope","col");
			th.innerText=colum[j];
			tr.appendChild(th);
		}
		the.appendChild(tr);
		tab.appendChild(the);
		var days=["MONDAY","TUESDAY","WEDNSDAY","THURSDAY","FRIDAY"];
		var tbody=document.createElement("tbody");
		for(j=0;j<5;j++){
			var tr=document.createElement("tr");
			tr.setAttribute("id",j+"row_")
			var tds=document.createElement("td");
			tds.innerText=days[j];
			tr.appendChild(tds);
			for(k=0;k<7;k++){
				var td=document.createElement("td");
				var br = document.createElement("br");
				var dbut=document.createElement("div")
				dbut.setAttribute("class","dropdown");
				var bu=document.createElement("button");
				bu.setAttribute("class","dropbtn");
				bu.setAttribute("id",`a${j}_${k}`);
                var ti='a'+j+'_'+k;
                bu.setAttribute("onclick","deselect("+"'"+ti+"'"+")");
            
				bu.style="height:35px;padding:3px;padding-top:1px:font-weight:bold;padding-bottom1px;font-size:12px";
				bu.innerText="fix";
				
				dbut.appendChild(bu);
				var ind=document.createElement("div");
				ind.setAttribute("class","dropdown-content");
				ind.setAttribute("id","cont");
               
				for(i=0;i<alloted.length;i++){
					var anchor=document.createElement("a");
					anchor.setAttribute("id",`a${j}_${k}_${i}`);
					anchor.setAttribute("href","#");
					anchor.setAttribute("class","fixlinks");
					var ta='a'+j+'_'+k+'_'+i+'';

					anchor.setAttribute("onclick","class_selected("+"'"+ta+"'"+")");
					anchor.innerText=alloted[i];
					ind.appendChild(anchor);
                 
				}
              
				/*dbut.onclick=function(){
                    console.log(ind);
                    console.log(ind.style)
				    var dis1=ind.style.display;
                    console.log(1000);
                    if(dis1!="block"){
                        ind.style="display:block";
                    }
                    else{
                        ind.style="display:none";
                    }
                }*/
                dbut.appendChild(ind);
				td.appendChild(dbut);
				tr.appendChild(td);
			}
			tbody.appendChild(tr);
		}
		tab.appendChild(tbody);
		block.appendChild(tab);
        block.style="position:relative;margin-right: auto; margin-left: auto;top:50px";
		var b=document.getElementsByClassName("block3");
		b[b.length-1].appendChild(block);

		var sb=document.getElementById("sub");
		if(sb!=null){
			$(sb.remove());
		}
		var bt =document.createElement("button");
		bt.setAttribute("class","dropbtn");
		bt.setAttribute("id","sub");
		bt.innerText="Save";
		bt.setAttribute("onclick","fac_submit()");
        bt.style="position:absolute;left:160px;top:250px;width:150px;height:30px;font-size:12px";
		var b=document.getElementsByClassName("block3");
		b[b.length-1].appendChild(bt);

	})
}
function deselect(n){
    console.log(n);
    var bu=n
    var req=document.getElementById(n);
    console.log(req);
    req.style="background-color:black";
    req.innerText="fix";
    var kc=document.getElementById("che"+bu.slice(1,2)+bu.slice(3,4));
    console.log(kc);
    var rem=document.querySelectorAll("#che"+bu.slice(1,2)+bu.slice(3,4));
    $(rem[rem.length - 1]).remove(); 
    var d=document.getElementsByTagName("td");
    console.log(d.length);
	var ele=(d.length/5);
    var ind=ele*parseInt(bu.slice(1,2))+parseInt(bu.slice(3,4))+1;
    console.log(ind);
    console.log(d[ind])
    var v=d[ind];
    var t=v.getElementsByTagName("br");
    console.log(t);
    var i=v.getElementsByTagName("p");
    v.removeChild(i[0]);
    v.removeChild(t[0]);


}
function class_selected(n){
	console.log(`${n}`);
	var bu=n.slice(0,-2);
	console.log(bu);
	var ele=document.getElementById(n);
	console.log(ele.innerText);
	var but=document.getElementById(bu);
	but.style="background-color:#dc3545 ;height:20px;font-weight:bold;overflow:hidden;text-overflow:ellipsis;padding:3px;padding-top:1px:padding-bottom1px;font-size:12px";
	but.innerText=ele.innerText;
	console.log(n.slice(1,2));
	console.log(n);
	var r=document.getElementById(n.slice(1,2)+"row_");
	var ds=r.getElementsByTagName("td");
	console.log(ds);
	console.log(r);
	var cl=n.slice(3,4);console.log(cl);
	var kc=document.getElementById("che"+bu.slice(1,2)+bu.slice(3,4));
    console.log(kc);
	if(kc==null){
	var cb=document.createElement("input");
	cb.setAttribute("type","checkbox");
	cb.setAttribute("value","lab?");
	cb.setAttribute("id","che"+bu.slice(1,2)+bu.slice(3,4));

	var br=document.createElement("br");
	ds[parseInt(cl)+1].appendChild(br);
	var text=document.createElement("p");
    text.innerText="Lab slot ";
    text.style="padding:2px;display:inline";
    ds[parseInt(cl)+1].appendChild(text);
    ds[parseInt(cl)+1].appendChild(cb);

	}
	/*var but=document.getElementById(`${m}`);
	but.innerText=ele.innerText;
*/
}



function stud_clicked(n){
	var c=document.getElementById("stud"+n);
	$.post("/stud_sel",{"selected":c.innerText},function(data,status){
		console.log(data.dic);
		var ar=data.dic;
		var facl=data.dic[0];
		var alloted= new Array();
		for(i=0;i<facl.length;i++){
			alloted.push(facl[i][1]);
		}
		var b=document.getElementsByClassName("block3");
		var alr=document.getElementsByTagName("h5");
		var nlr=document.getElementsByClassName("allotment");
		console.log(nlr,alr)
		if(alr.length!=0){
			$(alr[alr.length-1]).remove();
			console.log(nlr.length);
			if(nlr.length!=0){
				console.log(nlr)
				$(nlr[nlr.length-1].remove());
				console.log(alr.length);
			}
		}
		var name=document.createElement("h5");
		name.setAttribute("class","studfac");
		name.innerText=c.innerText;
        name.style="color:black;text-shadow: 0 0 20px white, 0 0 30px white, 0 0 40px white, 0 0 50px white, 0 0 60px white, 0 0 70px white, 0 0 80px white;position:relative;top:30px;text-align:center;font-size:30px"
		b[b.length-1].appendChild(name);
		var colum=["",1,2,3,4,5,6,7];
		var block=document.createElement("div")
		block.setAttribute("class","allotment");
		var tab=document.createElement("table");
		tab.setAttribute("class","table table-dark table-hover");
        tab.style="height:400px";
		the=document.createElement("thead");
		var tr=document.createElement("tr");
		var j;
		var k;
		for(j=0;j<colum.length;j++){
			var th=document.createElement("th");
			th.setAttribute("scope","col");
			th.innerText=colum[j];
			tr.appendChild(th);
		}
		the.appendChild(tr);
		tab.appendChild(the);
		var days=["MONDAY","TUESDAY","WEDNSDAY","THURSDAY","FRIDAY"];
		var tbody=document.createElement("tbody");
		for(j=0;j<5;j++){
			var tr=document.createElement("tr");
			tr.setAttribute("id",j+"row_");
			var tds=document.createElement("td");
			tds.innerText=days[j];
			tr.appendChild(tds);
			for(k=0;k<7;k++){
				var td=document.createElement("td");
				var br = document.createElement("br");
				var dbut=document.createElement("div")
				dbut.setAttribute("class","dropdown");
				var bu=document.createElement("button");
				bu.setAttribute("class","dropbtn");
                var ti='b'+j+'_'+k;
				bu.setAttribute("id",`b${j}_${k}`);
                bu.setAttribute("onclick","deselect("+"'"+ti+"'"+")");
				bu.style="height:35px;padding:3px;padding-top:1px:font-weight:bold;padding-bottom1px;font-size:12px";
				bu.innerText="fix";
				dbut.appendChild(bu);
				var ind=document.createElement("div");
				ind.setAttribute("class","dropdown-content");
				ind.setAttribute("id","cont");
				for(i=0;i<alloted.length;i++){
					var anchor=document.createElement("a");
					anchor.setAttribute("href","#");
					anchor.setAttribute("id",`b${j}_${k}_${i}`);
					anchor.setAttribute("class","fixlinks");
					var ta='b'+j+'_'+k+'_'+i+'';

					anchor.setAttribute("onclick","class_selected("+"'"+ta+"'"+")");
					anchor.innerText=alloted[i];
					ind.appendChild(anchor);
				}
				dbut.appendChild(ind);
                dbut.appendChild(ind);
				/*dbut.onclick=function(){
				var dis=ind.style.display;
                console.log(dis);
                if(dis!="block"){
                    ind.style="display:block";
                }
                else{
                    ind.style="display:none";
                }
                }*/
				td.appendChild(dbut);
				tr.appendChild(td);
			}
			tbody.appendChild(tr);
		}
		tab.appendChild(tbody);
		block.appendChild(tab);
        block.style="position:relative;margin-right: auto; margin-left: auto;top:50px";

		var b=document.getElementsByClassName("block3");
		var sb=document.getElementById("sub");
		b[b.length-1].appendChild(block);
		if(sb!=null){
			$(sb.remove());
		}
		var bt =document.createElement("button");
		bt.setAttribute("class","dropbtn");
		bt.setAttribute("id","sub")
		bt.innerText="Save";
		bt.setAttribute("onclick","class_submit()");
        bt.style="position:absolute;left:160px;top:250px;width:150px;height:30px;font-size:12px";
		var b=document.getElementsByClassName("block3");
		b[b.length-1].appendChild(bt);
	})
}

function class_submit(){
	var mar =new Array();
	var lab=new Array();
	var ar=document.getElementsByClassName("table table-dark table-hover");
	for(i=0;i<5;i++){
		var ar2=new Array();
		var ar1=new Array();
		var ro=document.getElementById(i+"row_");
		console.log(ro);
		var k=ro.getElementsByTagName("td");
		for(j=1;j<k.length;j++){
			if(k[j].innerText=="fix"){
				ar1.push("")
				ar2.push("");
			}
			else{
				var check=document.getElementById("che"+i+(j-1)).checked;
				console.log(check);
				if(check==true){
					ar2.push(k[j].innerText);
					ar1.push("");
				}
				else{
					ar1.push(k[j].innerText);
					ar2.push("");
				}
			}
		}
		lab.push(ar2);
		mar.push(ar1);
	}
	console.log(lab);
	console.log(mar);
	var head=document.getElementsByClassName("studfac");
	var te=head[0].innerText;
	console.log(te);

	$.post("/fix_submit_class",{"narr":`${mar}`,"labarr":`${lab}`,"name":`${te}`},function(data,status){
		var sv=document.getElementById("sub");
		sv.style="background-color:#dc3545;position:absolute;left:160px;top:250px;";
		sv.value="Saved";
		sv.innerText="Saved";
		console.log("success");
		var gt=document.getElementById("gb");
		if(gt!=null){
			$(gt.remove());
		}

	})


}


function fac_submit(){
	var mar =new Array();
	var lab=new Array();
	var ar=document.getElementsByClassName("table table-dark table-hover");
	for(i=0;i<5;i++){
		var ar2=new Array();
		var ar1=new Array();
		var ro=document.getElementById(i+"row_");
		console.log(ro);
		var k=ro.getElementsByTagName("td");
		for(j=1;j<k.length;j++){
			if(k[j].innerText=="fix"){
				ar1.push("")
				ar2.push("");
			}
			else{
				var check=document.getElementById("che"+i+(j-1)).checked;
				console.log(check);
				if(check==true){
					ar2.push(k[j].innerText);
					ar1.push("");
				}
				else{
					ar1.push(k[j].innerText);
					ar2.push("");
				}
			}
		}
		lab.push(ar2);
		mar.push(ar1);
	}
	console.log(lab);
	console.log(mar);
	var head=document.getElementsByClassName("namefac");
	var te=head[0].innerText;
	console.log(te);

	$.post("/fix_submit_class",{"narr":`${mar}`,"labarr":`${lab}`,"name":`${te}`},function(data,status){
		var sv=document.getElementById("sub");
		sv.style="background-color:#dc3545;position:absolute;left:160px;top:250px;";
		sv.innerText="Saved";
		var gt=document.getElementById("gb");
		if(gt!=null){
			$(gt.remove());
		}
		
	})


}


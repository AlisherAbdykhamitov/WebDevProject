import { Component } from '@angular/core';
import {CategoriesService} from './services/categories.service'
import { from } from 'rxjs';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Book-Shop';
  logged = false;

  username = '';
  password = '';

  constructor(private categoryService: CategoriesService) {}

  ngOnInit(){
    let token = localStorage.getItem('token');
    if (token){
      this.logged = true;
    }
  }

  login(){
    this.logged = true;
    // this.categoryService.login(this.username, this.password)
    //   .subscribe(res => {

    //     localStorage.setItem('token', res.token);
    //     this.logged = true;
      

    //     this.username = '';
    //     this.password = '';
    //   })
  }

  logout(){
    localStorage.clear();
    this.logged = false;
  }


}

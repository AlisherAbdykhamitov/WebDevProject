import { Component, OnInit } from '@angular/core';
import {Product} from '../data/products';
import {ProductDetailsService} from '../services/product-details.service';
import {ActivatedRoute} from '@angular/router';

@Component({
  selector: 'app-product-detail',
  templateUrl: './product-detail.component.html',
  styleUrls: ['./product-detail.component.css']
})
export class ProductDetailComponent implements OnInit {

  product: Product;
  constructor(private productDetailsService: ProductDetailsService, private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.getDetailsOfProduct();
  }

  getDetailsOfProduct(): any{
    const id = +this.route.snapshot.paramMap.get('id');
    this.productDetailsService.getDetailsOfProduct(id).subscribe(res => this.product = res);
  }
}

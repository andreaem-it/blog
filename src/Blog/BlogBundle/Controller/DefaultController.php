<?php

namespace Blog\BlogBundle\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\Controller;

class DefaultController extends Controller
{
    public function indexAction()
    {
    	//return $this->render('BlogBlogBundle:Template:header.html.twig');
        return $this->render('BlogBlogBundle::base.html.twig');
    }
}

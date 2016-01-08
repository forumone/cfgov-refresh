'use strict';

var BASE_JS_PATH = '../../../cfgov/unprocessed/js/';

var chai = require( 'chai' );
var sinon = require( 'sinon' );
var expect = chai.expect;
var jsdom = require( 'mocha-jsdom' );

describe( 'Get Event States', function() {
  var navPrimary;
  var sandbox;
  var link;
  var trigger;

  jsdom();

  before( function() {
    navPrimary = require( BASE_JS_PATH + 'modules/nav-primary.js' );
    sandbox = sinon.sandbox.create();
  } );

  beforeEach( function() {
    //  Adding a simplified version of the thing we want to test.
    document.body.innerHTML =
      '<button class="primary-nav_trigger js-primary-nav_trigger" ' +
      'aria-expanded="false"></button>' +
      '<nav class="js-primary-nav">' +
        '<div class="nav-item-1 js-primary-nav_item">' +
          '<a class="nav-link-1 js-primary-nav_link" ' +
             'href="http:// github.com">Link</a>' +
          '<div class="sub-nav-1 js-sub-nav" aria-expanded="false">' +
            '<button class="sub-nav-back-1 js-sub-nav_back">Back</button>' +
            '<a href="some-url">First Link</a>' +
          '</div>' +
        '</div>' +
        '<div class="nav-item-2 js-primary-nav_item">' +
          '<a class="nav-link-2 js-primary-nav_link" ' +
             'href="http:// github.com">Link</a>' +
          '<div class="sub-nav-2 js-sub-nav" aria-expanded="false">' +
            '<button class="js-sub-nav_back">Back</button>' +
            '<a href="some-url">First Link</a>' +
          '</div>' +
        '</div>' +
      '</nav>';
    navPrimary.init();
  } );

  afterEach( function() {
    sandbox.restore();
  } );

  describe( 'Primary Nav Link Events - Default state', function() {
    beforeEach( function() {
      link = document.querySelector( '.sub-nav-1 a' );
      var event = new Event( 'click', { bubbles: true } );
      document.querySelector( '.nav-link-1' ).dispatchEvent( event );
    } );

    it( 'should not navigate away from the page', function() {
      expect( window.location.href ).to.not.equal( 'http:// www.google.com/' );
    } );

    it( 'should toggle the sibling sub nav', function() {
      expect( document.querySelector( '.sub-nav-1' )
        .getAttribute( 'aria-expanded' ) ).to.equal( 'true' );
    } );

    it( 'should not toggle a non-sibling sub nav', function() {
      expect( document.querySelector( '.sub-nav-2' )
        .getAttribute( 'aria-expanded' ) ).to.equal( 'false' );
    } );

    it( 'should focus the first link in the sibling sub nav', function( done ) {
      setTimeout( function() { // eslint-disable-line max-nested-callbacks, no-inline-comments, max-len
        expect( link === document.activeElement ).to.be.true;
        done();
      }, 500 );
    } );

    it( 'should not focus the first link in a non-sibling sub nav',
      function( done ) {
        var nextlink = document.querySelector( '.sub-nav-2 a' );

        setTimeout( function() { // eslint-disable-line max-nested-callbacks, no-inline-comments, max-len
          expect( nextlink === document.activeElement ).to.be.false;
          done();
        }, 500 );
      } );
  } );

  describe( 'Primary Nav Link Events - One expanded', function() {
    beforeEach( function() {
      link = document.querySelector( '.sub-nav-2 a' );

      document.querySelector( '.sub-nav-1' )
        .getAttribute( 'aria-expanded', 'true' );
      var event = new Event( 'click', { bubbles: true } );
      document.querySelector( '.nav-link-2' ).dispatchEvent( event );
    } );

    it( 'should close others', function() {
      expect( document.querySelector( '.sub-nav-1' )
        .getAttribute( 'aria-expanded' ) ).to.equal( 'false' );
    } );

    it( 'should open the sibling sub nav', function( done ) {
      setTimeout( function() { // eslint-disable-line max-nested-callbacks, no-inline-comments, max-len
        expect( document.querySelector( '.sub-nav-2' )
          .getAttribute( 'aria-expanded' ) ).to.equal( 'true' );
        done();
      }, 500 );
    } );

    it( 'should focus the first link in sibling sub nav', function( done ) {
      setTimeout( function() { // eslint-disable-line max-nested-callbacks, no-inline-comments, max-len
        expect( link === document.activeElement ).to.be.true;
        done();
      }, 500 );
    } );

    it( 'should close itself', function( done ) {
      setTimeout( function() { // eslint-disable-line max-nested-callbacks, no-inline-comments, max-len
        var event = new Event( 'click', { bubbles: true } );
        var link2 = document.querySelector( '.nav-link-2' );
        link2.dispatchEvent( event );

        expect( link2.getAttribute( 'aria-expanded' ) ).to.equal( 'false' );
        done();
      }, 500 );
    } );

    it( 'should focus the primary link after closing', function( done ) {
      setTimeout( function() { // eslint-disable-line max-nested-callbacks, no-inline-comments, max-len
        var event = new Event( 'click', { bubbles: true } );
        var link2 = document.querySelector( '.nav-link-2' );
        link2.dispatchEvent( event );

        setTimeout( function() { // eslint-disable-line max-nested-callbacks, no-inline-comments, max-len
          expect( link2 === document.activeElement ).to.be.true;
          done();
        }, 500 );
      }, 500 );
    } );
  } );

  describe( 'Primary Nav Trigger Events', function() {
    beforeEach( function() {
      link = document.querySelector( '.nav-link-1' );
      trigger = document.querySelector( '.js-primary-nav_trigger' );
      trigger.dispatchEvent( new Event( 'click' ) );
    } );

    it( 'should open the primary nav', function() {
      expect( document.querySelector( '.js-primary-nav' )
        .getAttribute( 'aria-expanded' ) )
        .to.equal( 'true' );
    } );

    it( 'should focus the first primary link', function( done ) {
      setTimeout( function() { // eslint-disable-line max-nested-callbacks, no-inline-comments, max-len
        expect( link === document.activeElement ).to.be.true;
        done();
      }, 500 );
    } );

    it( 'should close the open primary nav', function() {
      trigger.dispatchEvent( new Event( 'click' ) );

      expect( document.querySelector( '.js-primary-nav' )
        .getAttribute( 'aria-expanded' ) )
        .to.equal( 'false' );
    } );

    it( 'should focus the trigger after closing', function( done ) {
      trigger.dispatchEvent( new Event( 'click' ) );

      setTimeout( function() { // eslint-disable-line max-nested-callbacks, no-inline-comments, max-len
        expect( trigger === document.activeElement )
          .to.be.true;
        done();
      }, 500 );
    } );
  } );

  describe( 'Sub Nav Back Events', function() {
    beforeEach( function() {
      link = document.querySelector( '.nav-link-1' );

      document.querySelector( '.sub-nav-1' )
        .getAttribute( 'aria-expanded', 'true' );
      document.querySelector( '.sub-nav-back-1' )
        .dispatchEvent( new Event( 'click' ) );
    } );

    it( 'should close the sub nav', function() {
      expect( document.querySelector( '.sub-nav-1' )
        .getAttribute( 'aria-expanded' ) )
        .to.equal( 'false' );
    } );

    it( 'should focus the primary link after closing', function( done ) {
      setTimeout( function() { // eslint-disable-line max-nested-callbacks, no-inline-comments, max-len
        expect( link === document.activeElement ).to.be.true;
        done();
      }, 500 );
    } );
  } );
} );

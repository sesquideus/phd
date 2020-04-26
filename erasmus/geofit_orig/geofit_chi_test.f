c   This program performs a non-linear fit to reflectance data by using
c   Hapke's development describing the reflectivity of an n-component
c   mixture given the optical constants of each individual component
c   and Singular Value Decomposition (SVD) techniques.
c   Also a number of parameters are defined in the parameter
c   statements.  The main subroutine defines some parameters and calls
c   The various subroutines that define different components of the
c   reflectivity calculation.  One integration is performed in the
c   calculation and if you wish the program to run faster, then you
c   should change the parameter "n" in the subroutine intg1.sub which is
c   called from old_ssc.sub and determines one component of the single
c   scattering efficiency.

c      INITIAL DEFINITIONS
c   both of these parameters must be changed in order to increase the
c   array sizes used throughout the program

c   maxwave - maximum number of wavelengths, real, and imaginary
c      indices of refraction
c   maxcomp - maximum number of individual components in the mixture
c   i2comp - two times maxcomp, represents the total number of free

c   INPUTS

c   m(i) - relative mass fraction of a component
c   rho(i) - solid density of a component
c   d(i) - particle diameter in millimeters
c   b(i) and c(i) - coefficients of the Legrende polynomial
c   beta(i) - factor that multiplies the Fresnel reflection coefficient
c      to give the fraction of light scattered from the surface of a
c      particle at g=0 (i.e. zero phase)
c   wve(i) - array containing wavelengths (in micrometers)
c   u - emergence angle (MEASURED FROM THE SURFACE NORMAL)
c       read in as the angle (in degrees) then converted to cosine
c       (in radians)
c   uo - incidence angle (MEASURED FROM THE SURFACE NORMAL)
c       read in as the angle (in degrees) then converted to cosine
c       (in radians)
c   g - phase angle (in degrees) then converted to radians
c   n(i,j) - array containing the real indices of refraction of each
c     component
c   nk(i,j) - array containing the imaginary indices of refraction of
c     each component
c   hi(i,j) - look up table for determining the values of 
c     Chandrasekhar's H-functions
c   comp - file containing optical constants of the ith component
c   outf - output file name
c   freq(i) - frequency (inverse centimeters) associated with each
c      wavelength
c   galb_m(i) - measured reflectance
c   galb_merr(i) - measured reflectance error

c   OUTPUT

c   galb_c(i) - calculated reflectivity of mixture relative to perfectly
c     reflecting surface.


c   INTERNAL PARAMETERS

c   debug - parameter used for debugging purposes
c   parray - array containg the mass fractions and particle diameters of
c      each component that is used in the SVD fitting proceedure

c   PROGRAM STRUCTURE

c           |-albinput.sub - gets the (1) measured data and errors
c           |                         (2) wavelengths and frequencies
c           |                         (3) real and imaginary indices
c           |                         (4) viewing geometry information
c           |                         (5) mass fractions and diameters
c           |
c   refl3.f -- refl.sub - calculates the reflectance
c           |           |
c           |           |-- cross_sec.sub
c           |           |-- old_ssc.sub
c           |                         |-- intg1.sub
c           |           |-- fr.sub
c           |           |-- phse.sub
c           |           |-- mulsc1.sub
c           |  
c           |- chisqrd.sub - calculates the chi squared value
c           |  
c           |- output.sub - writes out (1) final chi squared value
c                                      (2) wavelengths 
c                                      (3) final reflectances

      include 'geofit.inc'
      include 'declare.inc'
      character*80 outf
      integer nwave, ncomp, nsp, nintm, nscl
      real*8 m(maxcomp), d(maxcomp), area(maxcomp), galb_c(maxwave)
      real*8 alb_sperr(maxcomp,maxwave), alb_sp(maxcomp,maxwave)
      real*8 parray(i2comp), chisq
      real*8 p(i2comp+1,i2comp), y(i2comp+1), x(i2comp), e, ftol, u

c   read input parameters

      open(unit=99,file='chi_out.txt',status='new')
      debug=-1

      call albinput(ncomp,nwave,nsp,nintm,nscl,outf,m,rho,d,
     $b,c,beta,u,ftol,wve,freq,n,nk,hi,galb_m,galb_merr,area,
     $alb_sp,alb_sperr,x,debug)

      if (debug .eq. 0) then
        print *, 'data read in successfully'
        print *, nsp, nintm
        pause 2
      endif
      

c   prepare the parameter array 

      call prepare(ncomp,nsp,nintm,area,m,d,parray)

      if (debug .eq. 0) then
        print *, 'parameter array prepared'
        pause 3
      endif

c   calculate the function value for initial vertices of the simplex

      if ( (nintm .gt. 0) .and. (nsp .gt. 0) ) then
!           spatial & intimate mixture
!           spatial points first
        do i=1,nsp+1        ! spatial points first
          do j=1,nsp
            if (j .eq. i-1) then
              p(i,j) = parray(j)
            else
              p(i,j) = 1.25 * parray(j)
            endif
            x(j) = p(i,j)
          enddo
          call renorm(ncomp,nsp,nintm,x)
!          call energy(nwave,ncomp,nsp,nintm,nscl,ncalc,x,rho,b,
!     $              c,beta,wve,u,hi,alb_sp,alb_sperr,area,n,
!     $              nk,galb_m,galb_merr,galb_c,y(i),debug)
!     call chisqrd(nwave,galb_m,galb_merr,galb_c,chisq,debug)
        enddo
!           intimate points second
        do i=nsp+2,2*nintm+1+nsp+1
          do j=nsp+2,2*nintm+1+nsp
            if (j .eq. i-1) then
              p(i,j) = parray(j)
            else
              p(i,j) = 1.25 * parray(j)
            endif
            x(j) = p(i,j)
          enddo
!          call renorm(ncomp,nsp,nintm,x)
!          call energy(nwave,ncomp,nsp,nintm,nscl,ncalc,x,rho,b,
!     $              c,beta,wve,u,hi,alb_sp,alb_sperr,area,n,
!     $              nk,galb_m,galb_merr,galb_c,y(i),debug)
!     call chisqrd(nwave,galb_m,galb_merr,galb_c,chisq,debug)
        enddo
      elseif ( (nintm .le. 0) .and. (nsp .gt. 0) ) then
!           spatial mixture only
        do i=1,ncomp+1
          do j=1,ncomp
            if (j .eq. i-1) then
              p(i,j) = parray(j)
            else
              p(i,j) = 1.25 * parray(j)
            endif
            x(j) = p(i,j)
          enddo
          call renorm(ncomp,nsp,nintm,x)
!          call energy(nwave,ncomp,nsp,nintm,nscl,ncalc,x,rho,b,
!     $              c,beta,wve,u,hi,alb_sp,alb_sperr,area,n,
!     $              nk,galb_m,galb_merr,galb_c,y(i),debug)
!     call chisqrd(nwave,galb_m,galb_merr,galb_c,chisq,debug)
        enddo
      elseif ( (nintm .gt. 0) .and. (nsp .le. 0) ) then
!           intimate mixture only
!         write(20,*) 'initial vertices'
        do i=1,2*ncomp+1
          do j=1,2*ncomp
            if (j .eq. i-1) then
              p(i,j) = parray(j)
            else
              p(i,j) = 1.25 * parray(j)
            endif
            x(j) = p(i,j)
          enddo
          call renorm(ncomp,nsp,nintm,x)
          if (debug .eq. 0) then 
            print *, 'renormalize completed'
            pause 4
          endif
          call energy(nwave,ncomp,nsp,nintm,nscl,ncalc,x,rho,b,
     $              c,beta,wve,u,hi,alb_sp,alb_sperr,area,n,
     $              nk,galb_m,galb_merr,galb_c,y(i),debug)
          if (debug .eq. 0) then 
            print *, 'initial energies computed'
            pause 5
          endif
          call chisqrd(nwave,galb_m,galb_merr,galb_c,chisq,debug)
          if (debug .eq. 0) then           
            print *, 'chisqrd computed'
            pause 6
          endif
 !        write(99,100) (x(k),k=1,2*ncomp),chisq
 !         write(20,*) 'y(',i,')= ',y(i)
 !        do k=1,2*ncomp
 !           write(20,*) 'x(',k,')= ',x(k)
 !        enddo
        enddo
      endif
 
       print *, 'beginning vertices initialized'
!      do i=1,nwave
!        print *, wve(i), galb_m(i)
!      enddo
!
!      if ( (nintm .gt. 0) .and. (nsp .gt. 0) ) then
!        do i=1,nsp+1+2*nintm+1
!          print *, 'y(',i,')= ',y(i)
!        enddo
!      elseif ( (nintm .le. 0) .and. (nsp .gt. 0) ) then
!        do i=1,nsp+1
!          print *, 'y(',i,')= ',y(i)
!        enddo
!      elseif ( (nintm .gt. 0) .and. (nsp .le. 0) ) then
!        do i=1,2*nintm+1
!          print *, 'y(',i,')= ',y(i)
!        enddo
!      endif
!
!c   begin the simplex routine
!
       print *, 'simplex called'
 
       ncalc = 0
       call amoeba(nwave,ncomp,nsp,nintm,nscl,ncalc,parray,rho,b,
     $            c,beta,wve,u,n,nk,hi,galb_m,galb_merr,galb_c,
     $            p,y(i),ftol,iter,alb_sp,alb_sperr,debug)
 
       print *, 'simplex returned'
 
!c   evaluate the function at each final vertex
!
      if ( (nintm .gt. 0) .and. (nsp .gt. 0) ) then
!!           spatial & intimate mixture
!!           spatial points first
!        do i=1,nsp+1        ! spatial points first
!          do j=1,nsp
!            x(j) = p(i,j)
!          enddo
!          call renorm(ncomp,nsp,nintm,x)
!          call energy(nwave,ncomp,nsp,nintm,nscl,ncalc,x,rho,b,
!     $              c,beta,wve,u,hi,alb_sp,alb_sperr,area,n,
!     $              nk,galb_m,galb_merr,galb_c,y(i),debug)
!        enddo
!!           intimate points second
!        do i=nsp+2,2*nintm+1+nsp+1
!          do j=nsp+2,2*nintm+1+nsp
!            x(j) = p(i,j)
!          enddo
!          call renorm(ncomp,nsp,nintm,x)
!          call energy(nwave,ncomp,nsp,nintm,nscl,ncalc,x,rho,b,
!     $              c,beta,wve,u,hi,alb_sp,alb_sperr,area,n,
!     $              nk,galb_m,galb_merr,galb_c,y(i),debug)
!        enddo
      elseif ( (nintm .le. 0) .and. (nsp .gt. 0) ) then
!!           spatial mixture only
!        do i=1,ncomp+1
!          do j=1,ncomp
!            x(j) = p(i,j)
!          enddo
!          call renorm(ncomp,nsp,nintm,x)
!          call energy(nwave,ncomp,nsp,nintm,nscl,ncalc,x,rho,b,
!     $              c,beta,wve,u,hi,alb_sp,alb_sperr,area,n,
!     $              nk,galb_m,galb_merr,galb_c,y(i),debug)
!        enddo
       elseif ( (nintm .gt. 0) .and. (nsp .le. 0) ) then
!           intimate mixture only
c          write(20,*) 'final vertices'
        do i=1,2*ncomp+1
          do j=1,2*ncomp
            x(j) = p(i,j)
          enddo
          call renorm(ncomp,nsp,nintm,x)
          call energy(nwave,ncomp,nsp,nintm,nscl,ncalc,x,rho,b,
     $              c,beta,wve,u,hi,alb_sp,alb_sperr,area,n,
     $              nk,galb_m,galb_merr,galb_c,y(i),debug)
!c       write(20,*) 'y(',i,')= ',y(i)
!c       do k=1,2*ncomp
!c          write(20,*) 'x(',k,')= ',x(k)
!c       enddo
!       call chisqrd(nwave,galb_m,galb_merr,galb_c,chisq,debug)
!       write(99,100) (x(k),k=1,2*ncomp),chisq
        enddo
      endif
 
      if ( (nintm .gt. 0) .and. (nsp .gt. 0) ) then
        ncalc = ncalc - nsp + 1 - 2*nintm + 1
      elseif ( (nintm .le. 0) .and. (nsp .gt. 0) ) then
        ncalc = ncalc - ncomp + 1
      elseif ( (nintm .gt. 0) .and. (nsp .le. 0) ) then
        ncalc = ncalc - 2*nintm + 1
      endif
      print *, 'final energies calculated'

!c   determine the final vertex with the lowest energy value

      call minval(ncomp,nsp,nintm,p,x,y,ifit)
c       write(20,*) 'lowest value vertex'
c       write(20,*) 'y(',ifit,')= ',y(ifit)
c       do k=1,2*ncomp
c          write(20,*) 'x(',k,')= ',x(k)
c       enddo

      print *, 'minimum energy defined'

c   calculate the final geometric albedo using the lowest energy vertex

      call renorm(ncomp,nsp,nintm,x)
      call energy(nwave,ncomp,nsp,nintm,nscl,ncalc,x,rho,b,
     $           c,beta,wve,u,hi,alb_sp,alb_sperr,area,n,
     $           nk,galb_m,galb_merr,galb_c,e,debug)

      print *, 'final albedo calculated'

!c   write the solutions to the output file
      call chisqrd(nwave,galb_m,galb_merr,galb_c,chisq,debug)
!
      print *, 'writing output data'
!
      ncalc = ncalc - 1
!
      call output(ncomp,nwave,nsp,nintm,ncalc,outf,x,
     $            chisq,wve,freq,galb_c,debug)
      nc=2*ncomp
!
! 100  format(4(G12.5,2x),G12.5)
! 100  format(6(G11.4,1x),G11.4)
      STOP
      END

      include 'albinput.sub'
      include 'prepare.sub'
      include 'renorm.sub'
      include 'amoeba.sub'
      include 'minval.sub'
      include 'energy.sub'
      include 'output.sub'
      include 'galbcalc.sub'

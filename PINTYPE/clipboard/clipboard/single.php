<?php get_header(); ?>

	<div class="col2 single">

		<!-- content -->
		<?php if ( have_posts() ) { while ( have_posts() ) { the_post(); ?>

			<div class="postWrap">

				<?php get_template_part('template','post'); ?>

			</div><!-- end .postWrap -->
			
			<?php } // end while posts ?>

		<?php } // end if posts ?>


		<!-- social -->
		<?php if( get_post_meta($post->ID, 'vk_post_social', true )=='on' ) { ?>
			
			<div class="contentBlock navSocialBar entry_content">

				<?php get_template_part('template','social'); ?>

			</div><!-- end .contentBlock -->

		<?php } ?>


		<!-- navigation -->
		<?php if( get_post_meta($post->ID, 'vk_post_pagination', true )=='on' ) { ?>

			<div class="contentBlock navSocialBar entry_content">

				<div class="prevpost"><p><?php previous_post_link('%link','&larr; %title'); ?></p></div>

				<div class="nextpost"><p><?php next_post_link('%link','%title &rarr;'); ?></p></div>

			</div><!-- end .contentBlock -->

		<?php } ?>


		<!-- author -->
		<?php if(get_post_meta($post->ID, 'vk_post_author', true)=='on') { ?>
			
			<div class="contentBlock ar">

				<div class="entry_content">

					<div class="authorBadge">
						
						<!-- author -->
						<div class="authorAvatar">

							<?php $email='';

							$email = get_the_author_meta('user_email');

							$email = trim($email);

							$email = strtolower($email);

							$hash = md5( $email ); ?>

							<img src="http://www.gravatar.com/avatar/<?php echo $hash; ?>" />

							<a title="View all articles by <?php the_author(); ?>" href="<?php echo get_author_posts_url( get_the_author_meta( 'ID' ) ); ?>" class="button small accentButton fullwidth br"><?php _e('View all','framework'); ?></a>

						</div><!-- authorAvatar -->


						<div class="authorBio">

							<!-- name -->
							<h6><?php the_author(); ?></h6>
							
							<!-- description -->
							<p><?php the_author_meta('description'); ?></p>

							<?php // social vars
							$twitter = get_the_author_meta('twitter');

							$facebook = get_the_author_meta('facebook');

							$google = get_the_author_meta('google');

							$dribbble = get_the_author_meta('dribbble');

							$instagram =get_the_author_meta('instagram');

							$vine = get_the_author_meta('vine');

							$tumblr = get_the_author_meta('tumblr'); ?>

							<!-- social links -->
							<div class="authorSocial">

								<?php if($twitter!='') { ?>
									<a target="_blank" title="<?php echo $twitter; ?>" href="<?php echo $twitter; ?>" class="button small twitter">twitter</a>
								<?php } ?>

								<?php if($facebook!='') { ?>
									<a target="_blank" title="<?php echo $facebook; ?>" href="<?php echo $facebook; ?>" class="button small facebook">facebook</a>
								<?php } ?>

								<?php if($google!='') { ?>
									<a target="_blank" title="<?php echo $google; ?>" href="<?php echo $google; ?>" class="button small google">google</a>
								<?php } ?>

								<?php if($dribbble!='') { ?>
									<a target="_blank" title="<?php echo $dribbble; ?>" href="<?php echo $dribbble; ?>" class="button small dribbble">dribbble</a>
								<?php } ?>

								<?php if($instagram!='') { ?>
									<a target="_blank" title="<?php echo $instagram; ?>" href="<?php echo $instagram; ?>" class="button small instagram">instagram</a>
								<?php } ?>

								<?php if($vine!='') { ?>
									<a target="_blank" title="<?php echo $vine; ?>" href="<?php echo $vine; ?>" class="button small vine">vine</a>
								<?php } ?>

								<?php if($tumblr!='') { ?>
									<a target="_blank" title="<?php echo $tumblr; ?>" href="<?php echo $tumblr; ?>" class="button small tumblr">tumblr</a>
								<?php } ?>

							</div><!-- end .authorSocial -->

						</div><!-- end .authorBio -->

					</div><!-- end .authorBadge -->

				</div><!-- end .entry_content -->

			</div><!-- end .contentBlock -->

		<?php } ?>


		<!-- comments -->
		<?php if(get_post_meta($post->ID, 'vk_post_commments', true)=='on') {
			
			comments_template('', true); 

		} ?>

		<!-- similar -->
		<?php if(get_post_meta($post->ID, 'vk_post_similar', true)=='on') {
		
			if(has_tag()){
				
				// Get related posts by tag
				$related = vk_list_posts_by_tag( $post->ID, 10 );
				if ( $related ) {
					$args = array(
						'post__in'      => $related,
						'meta_key'=>'_thumbnail_id',			// Only with thumbnail
						'orderby'       => 'post__in',
						'no_found_rows' => true, // no need for pagination
					);

					$related = new WP_Query($args);
					if( $related->have_posts() ) { ?>

					<div class="similarWrap">

									<?php
									// set var
									$i=1;

									// foreach
									while( $related->have_posts() ) { $related->the_post();

									// thumb url
									$thumb = wp_get_attachment_image_src( get_post_thumbnail_id($post->ID), 'standard' );
									$url = $thumb['0'];
									?>

						<div class="similarPadding">
							<div class="contentBlock">
								<div class="entry_media">
									<div class="similarItem" style="background-image: url(<?php echo $url; ?>); ">

										<div class="entry_hover">
										<a href="<?php echo get_permalink(); ?>"></a>
										<div class="placement">
										<div class="iconWrap permalink">
										<a href="<?php echo get_permalink(); ?>"></a>
										<span class="icon-hyperlink"></span>
										</div>
										</div>
										</div>

									</div>
								</div>
							</div>
						</div>
									<?php $i++;

									}

					} wp_reset_postdata(); ?>

				</div>

				<?php } // end if related

			} // end if has tag

		} // end if similar on ?> 

	</div><!-- end col2 -->

	<!-- sidebar -->
	<div class="col1 postSidebar">

		<?php if(is_active_sidebar( 'post-1-sidebar' )) { dynamic_sidebar('post-1-sidebar'); } ?>

		<div id="floatStart" class="clear"></div>

		<div class="floatSidebar">

			<?php if(is_active_sidebar( 'post-2-sidebar' )) { dynamic_sidebar('post-2-sidebar'); } ?>

		</div><!-- end .floatSidebar -->

	</div><!-- end .postSidebar -->

<?php get_footer(); ?>
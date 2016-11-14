set (worlds
     empty.world
     pal_textured_object.world 
     reemc_indoor.world
     reemc.world
     simple_office.world
     small_office_door_obstacle.world
     small_office.world
     world_wall_REEM_photo.world
)

install(FILES ${worlds} DESTINATION ${CMAKE_INSTALL_PREFIX}/share/${PROJECT_NAME}/worlds/)
